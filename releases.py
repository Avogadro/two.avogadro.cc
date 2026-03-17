#!/usr/bin/env python3
import requests, json
from datetime import datetime

url = "https://api.github.com/repos/openchemistry/avogadrolibs/releases/latest"
release = requests.get(url).json()

def human_size(b): return f"{b/(1024*1024):.1f} MB"

def detect_platform(name):
    n = name.lower()
    if "darwin" in n or "mac" in n or "osx" in n or "dmg" in n:
        return "macOS-arm64" if any(a in n for a in ["arm","aarch64","silicon"]) else "macOS-x64"
    if "win" in n:
        return "windows-arm64" if "arm" in n else "windows-x64"
    if "linux" in n or "appimage" in n or "flatpak" in n:
        if "flatpak" in n: return "linux-flatpak"
        return "linux-arm64" if "aarch64" in n else "linux-x64"
    return "source" if n.endswith((".zip",".tar.gz")) else None

assets = []
for a in release["assets"]:
    plat = detect_platform(a["name"])
    if not plat: continue
    assets.append(dict(
        platform=plat,
        name=a["name"],
        url=a["browser_download_url"],
        size=human_size(a["size"])
    ))

data = {
    "version": release["tag_name"],
    "published": release["published_at"],
    "assets": assets
}

print(json.dumps(data, indent=2))
