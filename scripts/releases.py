#!/usr/bin/env python3
"""Fetch the latest Avogadro release info and update the install page.

Writes source/install/releases.json and updates the inline JSON block
and version-specific download URLs in source/install/index.md.

When the release is a new version 2.x, it also:
  * creates the release-notes page source/install/versions/v<slug>.md from
    the release body (only if the file does not already exist, so
    hand-edited pages are never overwritten),
  * lists that page first in the toctree of source/install/versions/avogadro2.md
    (if not already listed),
  * sets the version and its "Release Notes" link in source/install/index.md, and
  * updates the offline fallback version in source/conf.py.
Other major versions only get a warning; those steps are skipped.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import requests

REPO = "openchemistry/avogadrolibs"
API_URL = f"https://api.github.com/repos/{REPO}/releases/latest"
ROOT = Path(__file__).resolve().parent.parent / "source" / "install"
JSON_PATH = ROOT / "releases.json"
INDEX_PATH = ROOT / "index.md"
VERSIONS_DIR = ROOT / "versions"
TOCTREE_PATH = VERSIONS_DIR / "avogadro2.md"
CONF_PATH = ROOT.parent / "conf.py"
SUPPORTED_MAJOR = "2"

# The fallback release in conf.py, used when GitHub cannot be reached.
CONF_FALLBACK_RE = re.compile(
    r'(except requests\.exceptions\.ConnectionError:\s*\n\s*release = ")[^"]*(")'
)

# The option block that starts the toctree in avogadro2.md.
TOCTREE_RE = re.compile(r"(```\{toctree\}\n---\nmaxdepth: 1\n---\n)")

# The version and release-notes link in index.md, e.g.
#   v2.1.0 ([Release Notes](versions/v210.md))
NOTES_LINK_RE = re.compile(
    r"v[0-9][0-9.]* \(\[Release Notes\]\(versions/v[0-9]+\.md\)\)"
)

# GitHub doubles some links: [[text](url)](url) and [`[text](url)`](url)
DOUBLE_LINK_RE = re.compile(r"\[(`?)\[(.+?)\]\((?P<url>[^()\s]+)\)\1\]\((?P=url)\)")

# Pattern matching the download URL path with a version number, e.g.
#   /releases/download/1.103.0/Avogadro2-1.103.0-Darwin-arm64.dmg
# Captures the old version so we can replace it.
VERSION_URL_RE = re.compile(
    r"(/releases/download/)[0-9]+\.[0-9]+\.[0-9]+(/Avogadro2-)[0-9]+\.[0-9]+\.[0-9]+"
)

# Pattern matching the JSON block inside the <script> tag.
SCRIPT_JSON_RE = re.compile(
    r"(<script id='avogadro-release' type='application/json'>\n)"
    r".*?"
    r"(\n</script>)",
    re.DOTALL,
)


def human_size(b):
    return f"{b / (1024 * 1024):.1f} MB"


def detect_platform(name):
    n = name.lower()
    if "darwin" in n or "mac" in n or "osx" in n or "dmg" in n:
        return "macOS-arm64" if any(a in n for a in ["arm", "aarch64", "silicon"]) else "macOS-x64"
    if "win" in n:
        return "windows-arm64" if "arm" in n else "windows-x64"
    if "linux" in n or "appimage" in n or "flatpak" in n:
        if "flatpak" in n:
            return "linux-flatpak"
        return "linux-arm64" if "aarch64" in n else "linux-x64"
    return "source" if n.endswith((".zip", ".tar.gz")) else None


def clean_body(body):
    """Tidy a GitHub release body for use in a release-notes page."""
    body = body.replace("\r\n", "\n").replace("\r", "\n").strip()
    paragraphs = body.split("\n\n", 1)
    if paragraphs[0].startswith("We are pleased to announce"):
        body = paragraphs[1] if len(paragraphs) > 1 else ""
    body = DOUBLE_LINK_RE.sub(r"[\1\2\1](\g<url>)", body)
    return body.strip()


def format_date(published):
    """'2026-04-01T12:00:00Z' -> '1 April 2026' (no leading zero)."""
    d = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ")
    return f"{d.day} {d.strftime('%B %Y')}"


def create_notes_page(version, slug, published, body):
    """Write versions/v<slug>.md unless it already exists."""
    path = VERSIONS_DIR / f"v{slug}.md"
    if path.exists():
        print(f"{path} already exists; leaving it alone")
        return
    text = (
        f"(v{slug})=\n\n# Avogadro {version}\n\n"
        f"{format_date(published)}\n\n{clean_body(body)}\n"
    )
    path.write_text(text)
    print(f"Created {path}")


def add_to_toctree(slug):
    """Add the slug as the first toctree entry in avogadro2.md if missing."""
    text = TOCTREE_PATH.read_text()
    entry = f"v{slug}"
    if not TOCTREE_RE.search(text):
        print(f"Warning: toctree not found in {TOCTREE_PATH}")
        return
    block = text[TOCTREE_RE.search(text).end():].split("```", 1)[0]
    if entry in block.split():
        print(f"{entry} already in toctree")
        return
    text = TOCTREE_RE.sub(lambda m: m.group(1) + entry + "\n", text, count=1)
    TOCTREE_PATH.write_text(text)
    print(f"Added {entry} to {TOCTREE_PATH}")


def update_notes_link(version, slug):
    """Set the version and release-notes link (versions/v<slug>.md) in index.md."""
    if not (VERSIONS_DIR / f"v{slug}.md").exists():
        print(f"Warning: v{slug}.md not found; leaving the release-notes link alone")
        return
    text = INDEX_PATH.read_text()
    link = f"v{version} ([Release Notes](versions/v{slug}.md))"
    new, n = NOTES_LINK_RE.subn(lambda m: link, text, count=1)
    if n == 0:
        print(f"Warning: release-notes link not found in {INDEX_PATH}")
    elif new != text:
        INDEX_PATH.write_text(new)
        print(f"Updated release-notes link in {INDEX_PATH} to v{version}")


def update_conf_fallback(version):
    """Set the fallback release in conf.py (only that line)."""
    text = CONF_PATH.read_text()
    new, n = CONF_FALLBACK_RE.subn(
        lambda m: m.group(1) + version + m.group(2), text, count=1
    )
    if n == 0:
        print(f"Warning: fallback release not found in {CONF_PATH}")
    elif new != text:
        CONF_PATH.write_text(new)
        print(f"Updated fallback release in {CONF_PATH} to {version}")


def main():
    try:
        resp = requests.get(API_URL, timeout=10)
        resp.raise_for_status()
        release = resp.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching release info: {e}")
        sys.exit(1)

    assets = []
    for a in release["assets"]:
        plat = detect_platform(a["name"])
        if not plat:
            continue
        assets.append(dict(
            platform=plat,
            name=a["name"],
            url=a["browser_download_url"],
            size=human_size(a["size"]),
        ))

    data = {
        "version": release["tag_name"],
        "published": release["published_at"],
        "assets": assets,
    }

    version = data["version"]
    json_text = json.dumps(data, indent=2)

    # 1. Write releases.json
    JSON_PATH.write_text(json_text + "\n")
    print(f"Wrote {JSON_PATH}")

    # 2. Update index.md
    index = INDEX_PATH.read_text()

    # Replace version in download URLs (only versioned release URLs, not nightly/continuous)
    index = VERSION_URL_RE.sub(rf"\g<1>{version}\g<2>{version}", index)

    # Replace the inline JSON block
    index = SCRIPT_JSON_RE.sub(rf"\g<1>{json_text}\g<2>", index)

    INDEX_PATH.write_text(index)
    print(f"Updated {INDEX_PATH} to version {version}")

    # 3. Release notes page, toctree entry, index.md link and conf.py fallback
    if version.split(".")[0] != SUPPORTED_MAJOR:
        print(f"Warning: version {version} is not {SUPPORTED_MAJOR}.x; "
              "skipping release notes page, toctree, link and conf.py updates")
        return
    slug = version.replace(".", "")
    create_notes_page(version, slug, release["published_at"], release.get("body") or "")
    add_to_toctree(slug)
    update_notes_link(version, slug)
    update_conf_fallback(version)


if __name__ == "__main__":
    main()
