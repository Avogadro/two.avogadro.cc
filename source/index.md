---
notoc: true
html_theme.sidebar_secondary.remove: true
html_theme.show_prev_next: false
---

(about)=

Avogadro is an advanced molecule editor and visualizer designed for cross-platform use in computational chemistry, molecular modeling, bioinformatics, materials science, and related areas. It offers flexible high quality rendering and a powerful plugin architecture.

This documentation site is for Avogadro 2, currently in development.

::::{card-carousel} 3
:::{card}
![Thumbnail for benzene molecular orbital](/_static/benzene-mo.png)
:::
:::{card}
![Thumbnail for zeolite rendering](/_static/zeolite.png)
:::
:::{card}
![Thumbnail for QTAim analysis](/_static/phenol-qtaim.png)
:::
:::{card}
![Thumbnail for bond-centric editing](/_static/bondcentric.png)
:::
:::{card}
![Thumbnail for symmetry analysis of C180](/_static/C180.png)
:::
:::{card}
![Thumbnail for COVID spike protein](/_static/covid-spike.png)
:::
::::

## Install

::::{grid} 3
:::{grid-item-card}
:text-align: center
:class-header: sd-font-weight-bold sd-bg-light
{fab}`apple;fa-2x` MacOS
^^^
{{ '<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="' + macurl + '"><span>Download DMG</span></a>'}}
++++
<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_cmake/master/macOS.dmg.zip"><span>Download Nightly Build</span></a>
:::

:::{grid-item-card}
:text-align: center
:class-header: sd-font-weight-bold sd-bg-light
{fab}`windows;fa-2x` Windows
^^^
{{ '<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="' + winurl + '"><span>Download Installer</span></a>'}}
++++
<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_cmake/master/Win64.exe.zip"><span>Download Nightly Build</span></a>
:::

:::{grid-item-card}
:text-align: center
:class-header: sd-font-weight-bold sd-bg-light
{fab}`linux;fa-2x` Linux
^^^
{{ '<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="' + appurl + '"><span>Download AppImage</span></a>'}}
++++
<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="build.html"><span>Build from source</span></a>
:::

::::

## Features

- Free, Open Source: Easy to install and all source code and documentation is available to modify or extend.
- International: Translations into English, French, German, Hungarian, Indonesian, Japanese, Portuguese, Serbian, Turkish, and others, with [more languages to come](https://hosted.weblate.org/engage/avogadro/).
- Intuitive: Built to work easily for students and advanced researchers both.
- Fast: Supports multi-threaded rendering and computation.
- Extensible: Plugin architecture for developers, including rendering, interactive tools, commands, and Python scripts.

## Resources

::::{grid} 3
:::{grid-item-card}
:class-header: sd-font-weight-bold sd-bg-light sd-text-center
{fas}`book;fa-2x` User Guide
^^^

Coming Soon for Avogadro2:

- Getting Started
- Tutorials
- Manual
:::

:::{grid-item-card}
:class-header: sd-font-weight-bold sd-bg-light sd-text-center
{fas}`laptop-code;fa-2x` Develop
^^^

Develop scripts and C++ code with Avogadro:

- [Script Plugins](Scripts)
- Jupyter Notebooks
- [C++ API](API)

:::
:::{grid-item-card}
:class-header: sd-font-weight-bold sd-bg-light sd-text-center
{fas}`users;fa-2x` Contribute
^^^

We want your help to make Avogadro better for everyone:

- Roadmap
- [Translation / Localization](Translate)
- [Bugs / Issues][issues]
- [Feature Requests][features]
:::
::::

## Connecting with the Avogadro community

There are various ways to get in touch with the Avogadro community:

- [Avogadro Discussion] is the best place to ask questions and is a
  great way to get feedback from other users on how to approach a problem,
  suggest ideas, etc.
- If you think you've found a [bug][issues], or would like to request
a [feature][features], please report an issue on our [project tracker][tracker].
- You can also find more information about Avogadro on [Twitter] or <a rel="me" href="http://fosstodon.org/@avogadrochem">Mastodon</a>. Feel free to
  tag us on your papers and images!

```{toctree}
:hidden: true
:maxdepth: 2

install/index
docs/index
api/index
contrib/index
```

[avogadro discussion]: https://discuss.avogadro.cc/
[avogadrolibs github repository]: https://github.com/openchemistry/avogadrolibs
[features]: https://github.com/OpenChemistry/avogadrolibs/issues/new?template=feature_request.md
[issues]: https://github.com/OpenChemistry/avogadrolibs/issues/new?template=bug_report.md
[tracker]: https://github.com/openchemistry/avogadrolibs/issues
[twitter]: https://twitter.com/AvogadroChem
