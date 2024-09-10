---
notoc: true
html_theme.sidebar_secondary.remove: true
html_theme.show_prev_next: false
---

(about)=
# Avogadro

% One top-level grid with only rows, so that each text card is always next to the correct picture
:::::::{grid} 1
:gutter: 5
:padding: 5

% Now each row should be an adaptive grid, so that the text and image are side by side on monitors but stacked on mobile
% Use reverse for rows where the picture should be on the left
::::::{grid} 1 1 2 2
:gutter: 5

:::::{grid} 1
:gutter: 5

% Yet another nested grid so that the headline text and button are stacked
::::{grid-item}
:class: sd-font-weight-bold sd-fs-3 sd-text-primary
A free and open source molecular editor and visualization tool.
::::

::::{grid-item}
:::{button-ref} install
:color: primary
:shadow:
:expand:
Get Avogadro
:::
::::
:::::

:::::{grid-item-card}
:class-card: sd-border-0
:shadow: none
:img-background: /_static/home_screenshot_1.png
:::::
::::::

% Next row
::::::{grid} 1 1 2 2
:gutter: 5
:reverse:

:::::{grid-item-card} Flexible
:class-card: sd-border-0
:shadow: none
:class-title: sd-fs-4 sd-text-primary
Designed for students and advanced researchers alike.

Used in computational chemistry, molecular modeling, chemistry education, bioinformatics, materials science, and more.

Molecules, crystals, biomolecules, surfaces -- Avogadro loves them all.
:::::

:::::{grid-item-card}
:class-card: sd-border-0
:img-background: /_static/home_splash_1.png
:img-alt: Benzene with rendered molecular orbital
:::::
::::::

% Next row
::::::{grid} 1 1 2 2
:gutter: 5

:::::{grid-item-card} Intuitive
:class-card: sd-border-0
:shadow: none
:class-title: sd-fs-4 sd-text-primary
A sleek interface and user-friendly tools makes working in Avogadro easy, whether you are playing with molecules in 3D for the first time, quickly sketching structures for calculation input, or preparing graphics for publication.
:::::

:::::{grid-item-card}
:img-background: /_static/bondcentric.png
:img-alt: Bond-centric manipulation of a molecule
:::::
::::::

% Next row
::::::{grid} 1 1 2 2
:gutter: 5
:reverse:

:::::{grid-item-card} Beautiful
:class-card: sd-border-0
:shadow: none
:class-title: sd-fs-4 sd-text-primary
With a new, modern 3D renderer, visual effects like reflections and ambient occlusion, and a variety of display options, your molecules look good in Avogadro.

A picture paints a thousand words, but a movie tells a story -- make an animation to bring your chemistry to life.
:::::

:::::{grid-item-card}
:img-background: /_static/ferrocene.png
:img-alt: Ferrocene
:::::
::::::

% Next row
::::::{grid} 1 1 2 2
:gutter: 5

:::::{grid-item-card} Fast
:class-card: sd-border-0
:shadow: none
:class-title: sd-fs-4 sd-text-primary
Thanks to the rewritten core and lightning-quick multithreaded renderer, Avogadro 2 handles systems of thousands of atoms effortlessly.

Built-in force fields tidy up hand-drawn molecules in seconds.
:::::

:::::{grid-item-card}
:img-background: /_static/covid-spike.png
:img-alt: COVID-19 spike protein
:::::
::::::

% Next row
::::::{grid} 1 1 2 2
:gutter: 5
:reverse:

:::::{grid-item-card} Compatible
:class-card: sd-border-0
:shadow: none
:class-title: sd-fs-4 sd-text-primary
Read your geometry files, wherever they are from -- Avogadro understands a huge number of file formats, and can write to hundreds.

Explore the results of calculations with native output parsing for popular quantum chemistry programs including GAMESS, Gaussian, Molden, MOPAC, NWChem, and ORCA.
:::::
% Replace with a fancier looking molecular orbital render of some kind
:::::{grid-item-card}
:img-background: /_static/benzene-mo.png
:img-alt: Benzene with rendered molecular orbital
:::::
::::::

% Next row
::::::{grid} 1 1 2 2
:gutter: 5

:::::{grid-item-card} Extensible
:class-card: sd-border-0
:shadow: none
:class-title: sd-fs-4 sd-text-primary
Plugins add diverse functionality -- interactive tools, commands, interfaces to other programs, additional force fields and file formats, and more.

Writing your own plugin in Python is straightforward.
And if it's useful, why not share it with the community?
:::::

:::::{grid-item-card}
:img-background: /_static/zeolite.png
:img-alt: Zeolite rendering
:::::
::::::

% Next row
::::::{grid} 1 1 2 2
:gutter: 5
:reverse:

:::::{grid-item-card} Open
:class-card: sd-border-0
:shadow: none
:class-title: sd-fs-4 sd-text-primary
Avogadro is _free_, and all source code and documentation is available under the permissive BSD 3-clause license.

Got an issue?
The Avogadro community is friendly and ready to help.

Got an idea?
Development is public and contributions are welcomed.
:::::

:::::{grid-item-card}
:img-background: /_static/AuNP.png
:img-alt: A gold nanoparticle
:::::
::::::

% Next row
::::::{grid} 1 1 2 2
:gutter: 5

:::::{grid-item-card} International
:class-card: sd-border-0
:shadow: none
:class-title: sd-fs-4 sd-text-primary
Translations available for English, French, German, Hungarian, Indonesian, Japanese, Portuguese, Serbian, Turkish, and others, with [more languages to come](https://hosted.weblate.org/engage/avogadro/).
:::::

:::::{grid-item-card}
:img-background: /_static/C180.png
:img-alt: Symmetry analysis of C180
:::::
::::::

% Next row
::::::{grid} 1 1 2 2
:gutter: 5
:reverse:

:::::{grid-item-card} Cross-platform
:class-card: sd-border-0
:shadow: none
:class-title: sd-fs-4 sd-text-primary
Whether you use Windows, Linux, or macOS to get your work done, Avogadro is available and supported.

On ARM?
Apple Silicon is already supported, with Windows on ARM a future target.

The Qt base means Avogadro looks native and fits right in on your desktop.
:::::

:::::{grid-item-card}
:img-background: /_static/phenol-qtaim.png
:img-alt: QTAim analysis
:::::
::::::

:::::::


:::{button-ref} install
:color: primary
:shadow:
:expand:
Get Avogadro
:::


## Resources

:::::{grid}
:gutter: 3

::::{grid-item-card}
:columns: 4
:class-header: sd-font-weight-bold sd-bg-light sd-text-center sd-text-dark
:class-body: sd-text-center
{fas}`book;fa-2x` User Guide
^^^

Read the documentation and learn how to use Avogadro:

:::{button-ref} docs
:color: primary
:shadow:
:align: center
Guide
:::
:::{button-ref} getting-started
:color: primary
:outline:
:align: center
Getting started
:::
:::{button-ref} tutorials
:color: primary
:outline:
:align: center
Tutorials
:::
::::


::::{grid-item-card}
:columns: 4
:class-header: sd-font-weight-bold sd-bg-light sd-text-center sd-text-dark
:class-body: sd-text-center
{fas}`laptop-code;fa-2x` Development
^^^

Write Python scripts and C++ code for Avogadro:

:::{button-ref} develop
:color: primary
:shadow:
:align: center
Develop
:::
:::{button-ref} develop-scripts
:color: primary
:outline:
:align: center
Scripts
:::
:::{button-ref} develop-classlist
:color: primary
:outline:
:align: center
C++ API
:::
::::


::::{grid-item-card}
:columns: 4
:class-header: sd-font-weight-bold sd-bg-light sd-text-center sd-text-dark
:class-body: sd-text-center
{fas}`users;fa-2x` Get Involved
^^^

Help to make Avogadro better for everyone:

:::{button-ref} contrib
:color: primary
:shadow:
:align: center
Contribute
:::
:::{button-ref} Translate
:color: primary
:outline:
:align: center
Help with translation
:::
:::{button-ref} issues
:color: primary
:outline:
:align: center
Report a bug or issue
:::
:::{button-ref} features
:color: primary
:outline:
:align: center
Request a feature
:::
::::

::::{grid-item}
:columns: 2
::::

::::{grid-item-card}
:columns: 4
:class-header: sd-font-weight-bold sd-bg-light sd-text-center sd-text-dark
:class-body: sd-text-center
{fas}`graduation-cap;fa-2x` Education
^^^

Learn how Avogadro can be used in education:

:::{button-ref} teach
:color: primary
:shadow:
:align: center
Teach
:::
:::{button-ref} teaching-articles
:color: primary
:outline:
:align: center
Publications using Avogadro
:::
::::

::::{grid-item-card}
:columns: 4
:class-header: sd-font-weight-bold sd-bg-light sd-text-center sd-text-dark
:class-body: sd-text-center
{fas}`comments;fa-2x` Community
^^^

Ask questions, get feedback, and suggest ideas:

:::{button-ref} avogadro discussion
:color: primary
:shadow:
:align: center
Discuss
:::
:::{button-ref} https://fosstodon.org/@avogadrochem
:color: primary
:outline:
:align: center
Follow on Mastodon
:::
:::{button-ref} twitter
:color: primary
:outline:
:align: center
Follow on X
:::
:::{button-ref} tracker
:color: primary
:outline:
:align: center
GitHub project tracker
:::
::::

::::{grid-item}
:columns: 2
::::

:::::


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
