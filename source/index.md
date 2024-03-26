---
notoc: true
html_theme.sidebar_secondary.remove: true
html_theme.show_prev_next: false
---

(about)=
# Avogadro

Avogadro is a free and open source molecular editor and visualization tool.

It is highly capable and designed for use in computational chemistry, molecular modeling, chemistry education, bioinformatics, materials science, and related areas.

It offers flexible high-quality rendering, a modern UI with native styling, and a powerful plugin architecture.

Avogadro is designed for cross-platform use and is fully supported on macOS, Windows, and Linux.

This site is for the new Avogadro 2, currently in development.

::::{card-carousel} 3
% Only use images with aspect ratio of 5:4 so that they all match!
:::{card}
:img-background: /_static/benzene-mo.png
:img-alt: Benzene with rendered molecular orbital
:::
:::{card}
:img-background: /_static/covid-spike.png
:img-alt: COVID spike protein
:::
:::{card}
:img-background: /_static/ferrocene.png
:img-alt: Ferrocene
:::
:::{card}
:img-background: /_static/zeolite.png
:img-alt: Zeolite rendering
:::
:::{card}
:img-background: /_static/C180.png
:img-alt: Symmetry analysis of C180

:::
:::{card}
:img-background: /_static/bondcentric.png
:img-alt: Bond-centric editing
:::
:::{card}
:img-background: /_static/AuNP.png
:img-alt: A gold nanoparticle
:::
:::{card}
:img-background: /_static/phenol-qtaim.png
:img-alt: QTAim analysis
:::
::::

## Install

::::{grid} 3
:::{grid-item-card}
:text-align: center
:class-header: sd-font-weight-bold sd-bg-light sd-text-dark
{fab}`apple;fa-2x` macOS
^^^
{{ '<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="' + macurl + '"><span>Download DMG</span></a>'}}
++++
<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_cmake/master/macOS.dmg.zip"><span>Download Nightly Build</span></a>
:::

:::{grid-item-card}
:text-align: center
:class-header: sd-font-weight-bold sd-bg-light sd-text-dark
{fab}`windows;fa-2x` Windows
^^^
{{ '<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="' + winurl + '"><span>Download Installer</span></a>'}}
++++
<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="https://nightly.link/OpenChemistry/avogadrolibs/workflows/build_cmake/master/Win64.exe.zip"><span>Download Nightly Build</span></a>
:::

:::{grid-item-card}
:text-align: center
:class-header: sd-font-weight-bold sd-bg-light sd-text-dark
{fab}`linux;fa-2x` Linux
^^^
{{ '<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="' + appurl + '"><span>Download AppImage</span></a>'}}
++++
<a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-outline-primary reference external" href="install/build.html"><span>Build from source</span></a>
:::

::::

## Features

- **Free, Open Source**: Easy to install and all source code and documentation is available to modify or extend.
- **International**: Translations into English, French, German, Hungarian, Indonesian, Japanese, Portuguese, Serbian, Turkish, and others, with [more languages to come](https://hosted.weblate.org/engage/avogadro/).
- **Intuitive**: Built to work easily for students and advanced researchers both.
- **Fast**: Supports multi-threaded rendering and computation.
- **Extensible**: Plugin architecture for developers, including rendering, interactive tools, commands, and Python scripts.

## Resources

::::{grid} 3
:::{grid-item-card}
:class-header: sd-font-weight-bold sd-bg-light sd-text-center sd-text-dark
{fas}`book;fa-2x` User Guide
^^^

Coming Soon for Avogadro 2:

- [Getting Started](getting-started)
- [Manual](docs)
- [Tutorials](tutorials)
:::

:::{grid-item-card}
:class-header: sd-font-weight-bold sd-bg-light sd-text-center sd-text-dark
{fas}`laptop-code;fa-2x` Develop
^^^

Develop scripts and C++ code with Avogadro:

- [Script Plugins](Scripts)
- Jupyter Notebooks
- [C++ API](develop)

:::
:::{grid-item-card}
:class-header: sd-font-weight-bold sd-bg-light sd-text-center sd-text-dark
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
develop/index
contrib/index
teach/index
```

[avogadro discussion]: https://discuss.avogadro.cc/
[avogadrolibs github repository]: https://github.com/openchemistry/avogadrolibs
[features]: https://github.com/OpenChemistry/avogadrolibs/issues/new?template=feature_request.md
[issues]: https://github.com/OpenChemistry/avogadrolibs/issues/new?template=bug_report.md
[tracker]: https://github.com/openchemistry/avogadrolibs/issues
[twitter]: https://twitter.com/AvogadroChem
