(install)=

# Install

Most users will want to use the current official release ({{release}}).

If you have problems using the current release or want to use the latest features, try out one of the **"nightly" builds** created every night from the current source code, which contains all improvements and bug fixes since the last release.

We're open-source, so if you would like to compile Avogadro yourself from the code, you can – see [Building Source Code](install-build).


::::::{grid} 3
:gutter: 0

% Title row
::::{grid-item}
% Empty
::::


::::{grid-item-card}
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light
Current Release ({{release}})
::::


::::{grid-item-card}
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light
Nightly Build
::::


% Mac row
::::{grid-item-card}
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light
{fab}`apple;fa-2x` macOS
::::


::::{grid-item-card}
:text-align: center
:shadow: none

:::{button-link} {{macurl}}
:color: primary
:outline:
Download DMG
:::
::::


::::{grid-item-card}
:text-align: center
:shadow: none

:::{button-link} https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_cmake/master/macOS.dmg.zip
:color: secondary
:outline:
Download Nightly Build
:::
::::


% Windows row
::::{grid-item-card}
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light
{fab}`windows;fa-2x` Windows
::::


::::{grid-item-card}
:text-align: center
:shadow: none

:::{button-link} {{winurl}}
:color: primary
:outline:
Download Installer
:::
::::


::::{grid-item-card}
:text-align: center
:shadow: none

:::{button-link} https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_cmake/master/Win64.exe.zip
:color: secondary
:outline:
Download Nightly Build
:::
::::


% Linux row
::::{grid-item-card}
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light
{fab}`linux;fa-2x` Linux
::::

::::{grid-item-card}
:text-align: center
:shadow: none

:::{button-link} {{appurl}}
:color: primary
:outline:
Download AppImage
:::

:::{button-link} https://flathub.org/apps/org.openchemistry.Avogadro2
:color: primary
:outline:
Download Flatpak
:::

:::{button-link} https://repology.org/project/avogadro2/versions
:color: primary
:outline:
Check your distro's repositories
:::
::::


::::{grid-item-card}
:text-align: center
:shadow: none

:::{button-link} https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_cmake/master/Avogadro2.AppImage.zip
:color: secondary
:outline:
Nightly AppImage
:::
::::


% BSD row
::::{grid-item-card}
:text-align: center
:shadow: none
:class-card: sd-font-weight-bold sd-bg-light
{fab}`freebsd;fa-2x` FreeBSD
::::

::::{grid-item-card}
:text-align: center
:shadow: none

:::{button-link} https://www.freshports.org/science/avogadro2/
:color: primary
:outline:
`pkg install avogadro2`
:::
::::

::::{grid-item-card}
:text-align: center
:shadow: none
% Empty
::::


::::::


```{toctree}
---
hidden: true
caption: Installation
---
self
build
versions/index
```
