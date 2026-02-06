(install)=

# Install

Most users will want to use the current official release:

<div class="sd-col sd-d-flex-column docutils">
<span class="sd-d-grid"><a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-primary sd-shadow-sm" id="download-button" href="#">Detecting OS…</a></span>
<p id="download-info" class="sd-bg-light sd-text-dark sd-text-center sd-font-weight-bold"></p>
</div>

If you have problems using the current release or want to use the latest features, try out one of the **"nightly" builds** continually created from the current source code, which contains all improvements and bug fixes since the last release.

We're open-source, so if you would like to compile Avogadro yourself from the code, you can -- see [Building Source Code](develop-build) for more on how.


::::::{grid}
:gutter: 0

% Title row
::::{grid-item}
:columns: 4 4 2 2
% Empty
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light sd-text-dark
Current Release ({{release}})
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light sd-text-dark
Nightly Build
::::


% Mac row
::::{grid-item-card}
:columns: 4 4 2 2
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light sd-text-dark
:class-row: sd-d-flex-column
{fab}`apple;fa-2x`

macOS
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/latest/download/Avogadro2-1.102.1-Darwin-arm64.dmg
:ref-type: myst
:color: primary
:outline:
Download DMG (Apple Silicon)
:::

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/latest/download/Avogadro2-1.102.1-Darwin.dmg
:color: primary
:outline:
Download DMG (Intel)
:::
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/download/continuous/Avogadro2-continuous-arm64.dmg
:color: secondary
:outline:
Download Nightly (Apple Silicon)
:::

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/download/continuous/Avogadro2-continuous.dmg
:color: secondary
:outline:
Download Nightly (Intel)
:::
::::


% Windows row
::::{grid-item-card}
:columns: 4 4 2 2
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light sd-text-dark
:class-row: sd-d-flex-column
{fab}`windows;fa-2x`

Windows
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/latest/download/Avogadro2-1.102.1-win64.exe
:color: primary
:outline:
Download Installer
:::
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/download/continuous/Avogadro2-continuous-win64.exe
:color: secondary
:outline:
Download Nightly Build
:::
::::


% Linux row
::::{grid-item-card}
:columns: 4 4 2 2
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light sd-text-dark
:class-row: sd-d-flex-column
{fab}`linux;fa-2x`

Linux
::::

::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/latest/download/Avogadro2-x86_64.AppImage
:color: primary
:outline:
Download AppImage
:::

:::{button-link} https://flathub.org/apps/org.openchemistry.Avogadro2
:color: primary
:outline:
Install the Flatpak
:::

:::{button-link} https://repology.org/project/avogadro2/versions
:color: primary
:outline:
Check your distro's repositories
:::
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/download/continuous/Avogadro2-x86_64.AppImage
:color: secondary
:outline:
Nightly AppImage
:::

:::{button-ref} install-flatpak-beta
:color: secondary
:outline:
Install the Beta Flatpak
:::
::::


% BSD row
::::{grid-item-card}
:columns: 4 4 2 2
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light sd-text-dark
{fab}`freebsd;fa-2x`

FreeBSD
::::

::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://www.freshports.org/science/avogadro2/
:color: primary
:outline:
`pkg install avogadro2`
:::
::::

::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none
% Empty
::::


% Source code row
::::{grid-item-card}
:columns: 4 4 2 2
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light sd-text-dark
{fas}`code;fa-2x`

Source Code
::::

::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/latest/
:color: primary
:outline:
`avogadrolibs`
:::
:::{button-link} https://github.com/OpenChemistry/avogadroapp/releases/latest/
:color: primary
:outline:
`avogadroapp`
:::
::::

::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://github.com/OpenChemistry/avogadrolibs
:color: secondary
:outline:
Avogadro on GitHub {fab}`github;fa-1x`
:::
::::

::::::

<!-- JSON inserted here by Python script -->
<script id='avogadro-release' type='application/json' src="releases.json">
{
  "version": "1.103.0",
  "published": "2026-02-06T12:01:13Z",
  "assets": [
    {
      "platform": "macOS-arm64",
      "name": "Avogadro2-1.103.0-Darwin-arm64.dmg",
      "url": "https://github.com/OpenChemistry/avogadrolibs/releases/download/1.103.0/Avogadro2-1.103.0-Darwin-arm64.dmg",
      "size": "85.8 MB"
    },
    {
      "platform": "macOS-x64",
      "name": "Avogadro2-1.103.0-Darwin.dmg",
      "url": "https://github.com/OpenChemistry/avogadrolibs/releases/download/1.103.0/Avogadro2-1.103.0-Darwin.dmg",
      "size": "90.3 MB"
    },
    {
      "platform": "windows-x64",
      "name": "Avogadro2-1.103.0-win64.exe",
      "url": "https://github.com/OpenChemistry/avogadrolibs/releases/download/1.103.0/Avogadro2-1.103.0-win64.exe",
      "size": "113.7 MB"
    },
    {
      "platform": "linux-arm64",
      "name": "Avogadro2-aarch64.AppImage",
      "url": "https://github.com/OpenChemistry/avogadrolibs/releases/download/1.103.0/Avogadro2-aarch64.AppImage",
      "size": "105.5 MB"
    },
    {
      "platform": "linux-x64",
      "name": "Avogadro2-x86_64.AppImage",
      "url": "https://github.com/OpenChemistry/avogadrolibs/releases/download/1.103.0/Avogadro2-x86_64.AppImage",
      "size": "104.2 MB"
    }
  ]
}
</script>

<script>
function getMacOSArchitecture() {
  const canvas = document.createElement('canvas');
  const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');

  if (gl) {
    const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
    if (debugInfo) {
      const renderer = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);

      if (/Apple (M\d|GPU)/.test(renderer)) {
        return 'arm64';
      } else if (/Intel/.test(renderer)) {
        return 'x86_64';
      }
    }
  }

  return 'unknown';
}

function detectPlatform() {
  const ua = navigator.userAgent.toLowerCase();
  const isARM = /arm|aarch64|apple silicon/.test(ua);
  if (ua.includes("win")) return isARM ? "windows-arm64" : "windows-x64";
  if (ua.includes("mac")) {
    const arch = getMacOSArchitecture();
    if (arch === 'arm64') return 'macOS-arm64';
    if (arch === 'x86_64') return 'macOS-x64';
  }
  if (ua.includes("linux")) return isARM ? "linux-arm64" : "linux-x64";
  return "unknown";
}

// Get icon for platform
function getIcon(iconName) {
    const icons = {
        'windows': '<i class="fab fa-windows"></i>',
        'macOS': '<i class="fab fa-apple"></i>',
        'linux': '<i class="fas fa-code"></i>'
    };
    return icons[iconName] || '📦';
}

// Get label for platform
function platLabel(platform) {
    const label = {
      "windows-x64":"Windows (x64)",
      "windows-arm64":"Windows (ARM64)",
      "macOS-x64":"macOS (Intel)",
      "macOS-arm64":"macOS (Apple Silicon)",
      "linux-x64":"Linux (x64 AppImage)",
      "linux-arm64":"Linux (ARM AppImage)",
      "linux-flatpak":"Linux (Flatpak)",
      "source":"Source Code"
    };
    return label[platform] || platform;
}

document.addEventListener("DOMContentLoaded", () => {
  const data = JSON.parse(document.getElementById("avogadro-release").textContent);
  const platform = detectPlatform();
  const btn = document.getElementById("download-button");
  const info = document.getElementById("download-info");

  const asset = data.assets.find(a => a.platform === platform);
  const label = platLabel(platform);

  if (asset) {
    btn.href = asset.url;
    btn.textContent = `Download Avogadro ${data.version}`;
    info.textContent = `${label} • ${data.version} • ${asset.size} • ${new Date(data.published).toLocaleDateString()}`;
  } else {
    btn.textContent = "See All Downloads";
    btn.href = "#fallback-table";
  }
});
</script>


```{toctree}
---
hidden: true
caption: Installation
---
self
flatpak
versions/index
```
