#!/usr/bin/env python3
"""Fetch the latest Avogadro release info and update the install page.

Writes source/install/releases.json and updates the inline JSON block
and version-specific download URLs in source/install/index.md.
"""
import json
import re
from pathlib import Path

import requests

REPO = "openchemistry/avogadrolibs"
API_URL = f"https://api.github.com/repos/{REPO}/releases/latest"
ROOT = Path(__file__).resolve().parent.parent / "source" / "install"
JSON_PATH = ROOT / "releases.json"
INDEX_PATH = ROOT / "index.md"

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


def main():
    release = requests.get(API_URL).json()

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


if __name__ == "__main__":
    main()
