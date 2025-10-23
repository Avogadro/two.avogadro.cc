(install)=

# Install

Most users will want to use the current official release ({{release}}).

If you have problems using the current release or want to use the latest features, try out one of the **"nightly" builds** created every night from the current source code, which contains all improvements and bug fixes since the last release.

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
{fab}`apple;fa-2x`

macOS
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/latest/download/Avogadro2-1.102.0-Darwin-arm64.dmg
:ref-type: myst
:color: primary
:outline:
Download DMG (Apple Silicon)
:::

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/latest/download/Avogadro2-1.102.0-Darwin.dmg
:color: primary
:outline:
Download DMG (Intel)
:::
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_mac/master/macOS-arm64.zip
:color: secondary
:outline:
Download Nightly Build (Apple Silicon)
:::

:::{button-link} https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_mac/master/macOS-intel.zip
:color: secondary
:outline:
Download Nightly Build (Intel)
:::
::::


% Windows row
::::{grid-item-card}
:columns: 4 4 2 2
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light sd-text-dark
{fab}`windows;fa-2x`

Windows
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://github.com/OpenChemistry/avogadrolibs/releases/latest/download/Avogadro2-1.102.0-win64.exe
:color: primary
:outline:
Download Installer
:::
::::


::::{grid-item-card}
:columns: 4 4 5 5
:text-align: center
:shadow: none

:::{button-link} https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_windows/master/Win64.exe.zip
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

:::{button-link} https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_linux/master/Avogadro2-x86_64.AppImage.zip
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


```{toctree}
---
hidden: true
caption: Installation
---
self
flatpak
versions/index
```
