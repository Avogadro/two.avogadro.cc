(develop-build)=

# Building Source Code

This guide has been updated to include detailed instructions for compiling Avogadro on each major operating system and has been verified to work for the 2.0 release on all of them.

However, Avogadro is a large project with many pieces, resulting in a somewhat complex build process that also varies from platform to platform.
If you encounter difficulties you are encouraged to reach out on the [forum](https://discuss.avogadro.cc) for help.

The Avogadro desktop application brings together several of the Open Chemistry subprojects (see [Project Structure](develop-structure)).
The easiest way to build Avogadro is to use the [openchemistry
repository](https://github.com/OpenChemistry/openchemistry) as a basis, as it will automatically download and build many of the dependencies (including third-party ones) for you.

It is also entirely possible to build each project individually without using the "superbuild" approach, but you will need to ensure all dependencies are built and can be found by the project.

For simplicity, this guide will focus on the first approach.

:::{tip}
Platform-specific instructions, guidance, and information is provided in expandable callouts marked by the respective icons {fab}`windows` {fab}`apple` {fab}`linux`.
:::


## System

Only 64-bit operated systems are supported.

The primary supported operating systems are those for which binaries are distributed:

- Windows 10+ (`x64` only)
- macOS (Intel and Apple Silicon)
- Linux (`x64` only)

Others may work, but this guide will not cover them.

:::{admonition} Windows on ARM {fab}`windows`
:class: dropdown
Windows on ARM will be fully supported by Qt from around Qt 6.8 onwards, so it is likely that Avogadro will likewise support ARM once the port to Qt6 is complete.
:::

## Dependencies and prerequisites

:::{admonition} Windows {fab}`windows`
:class: dropdown
All the software listed here can of course be obtained in the traditional way by downloading from the respective websites, which are generally linked, and running an installer.

Alternatively, much of it can these days be obtained from the Windows Package Manager using [`winget`](https://learn.microsoft.com/en-us/windows/package-manager/winget/).

The third-party [winget.run](https://winget.run/) can be a helpful site to see whether a package is available in this way.
:::

:::{admonition} macOS {fab}`apple`
:class: dropdown
The [Homebrew](https://brew.sh/) package manager works well for getting development software on macOS.
:::

:::{admonition} Linux {fab}`linux`
:class: dropdown
On Linux, all of the necessary (non-Open-Chemistry) software is almost certainly available via your distribution's package manager.

A notable exception to this is Open Babel, which as of the time of writing (September 2024) is generally only available from distro repos as version 3.3.1, whereas Avogadro requires a patched version incorporating many CJSON-related changes over the past few years.

The easiest thing is just to let the build process automatically download and compile Open Babel for you (the default behavior).
If you particularly wish to use Open Babel from your system, you will have to have compiled it from [source](https://github.com/openbabel/openbabel) yourself.
:::

### Development tools

The Open Chemistry project uses [Git](https://git-scm.com/) for version control, and [CMake](cmake.org) to direct the build process, so the first step is to ensure that you have both of these installed and set up on your system.


### Compiler

Broadly, you will need a C/C++ compiler that supports C++17.

:::{admonition} Windows {fab}`windows`
:class: dropdown
On Windows, [Visual Studio](https://visualstudio.microsoft.com/) is best supported, and it includes the MSVC compiler.
:::

:::{admonition} macOS {fab}`apple`
:class: dropdown
We recommend to use [Clang 17](https://clang.llvm.org/) on a Mac.
:::

:::{admonition} Linux {fab}`linux`
:class: dropdown
Both `gcc`/`g++` and `clang`/`clang++` generally work fine, as do both Unix Makefiles and Ninja for generating the Make files.

If in doubt, stick to the combination of **gcc with Ninja**; this is what the automatic preparation of Avogadro binaries with GitHub actions uses, so if it is working successfully there, it should also work for you.
:::


### Python and Perl

To compile Avogadro you will need to have both Python and Perl on your system.

It is important that Python is in the PATH so that Avogadro can find it.

:::{admonition} Windows {fab}`windows`
:class: dropdown
A Python interpreter can be downloaded and installed from [python.org](https://www.python.org/downloads/windows/).
The option to add to the PATH is offered at install time, so make sure to check this.

The best way to get Perl on Windows is the [Strawberry Perl](https://strawberryperl.com/) distribution.
:::


### Libraries

#### Qt

Avogadro is built using the open-source [Qt framework](https://www.qt.io/download-open-source).

Avogadro is in the process of moving to Qt6, which will be hopefully complete by the release of Avogadro 2.0 – see [the forum tracking thread](https://discuss.avogadro.cc/t/qt6-tracking-thread/5592) for progress.
For now though, you will probably need to obtain Qt5.

:::{admonition} Windows {fab}`windows`
:class: dropdown
On Windows you should download and install Qt from the Qt website.

Be sure to make a note of the install directory of Qt (e.g. `C:/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5`) as it will be of importance later.
:::

:::{admonition} Linux {fab}`linux`
:class: dropdown
Qt is widely used in the open-source community, including as the base for the KDE Plasma desktop environment, so it is generally either already installed (though not necessarily including the development libraries that you need) or easily available from package managers.

Qt is large, so on Linux distributions it is often broken up into its modules.
Unfortunately, the names of the packages for the modules varies from distro to distro, such that it is hard to say exactly which packages you should install.

You should however make sure the following Qt modules are installed:

- `QtCore`
- `QtWidgets`
- `QtGui`
- `QtOpenGL`
- `QtConcurrent`
- `QtNetwork`
- `QtSvg`

If building with Qt6, you will also need:

- `QtOpenGLWidgets`
- `QtCore5Compat`

There are often separate `-devel` versions of each module as well, in which case, you will also need those.
:::

:::{admonition} Debian/Ubuntu-based distributions {fab}`linux`
:class: dropdown 

You can install prerequisites with the following commands:

```bash
apt-get update && \
 apt-get install -y cmake curl build-essential qtbase5-dev qtdeclarative5-dev zlib1g-dev libxml2-dev git libqt5svg5-dev libqt5gui5 libqt5concurrent5 rapidjson && \
```
If you need a newer cmake version (replace aarch64 with your architecture or go to [CMake Releases](https://github.com/Kitware/CMake/releases/latest/))
```bash
apt-get purge cmake && \
 curl -L -v -o /tmp/bin https://github.com/Kitware/CMake/releases/download/v3.26.5/cmake-3.26.5-linux-aarch64.sh && \
 chmod +x /tmp/bin && \
 cd /usr && \
 /tmp/bin
```
:::

:::{admonition} openSUSE Tumbleweed {fab}`linux`
:class: dropdown

Many of the following may already be installed on your system.

```bash
sudo zypper refresh
sudo zypper install libqt5-qtbase libqt5-qtbase-devel libqt5-qtbase-common-devel glew-devel libOpenGL Spglib libarchive libxml2 glu readline xz libeigen3 libboost
```

The `libqt5-qtbase*` patterns should include all the Qt dependencies you need, but it is worth checking that all the modules are installed still using:

```bash
sudo zypper search libQt5
```
:::

:::{admonition} Fedora {fab}`linux`
:class: dropdown

```bash
sudo dnf update
sudo dnf install -y cmake gcc gcc-g++ qt5-qtbase-devel zlib-devel libxml2-devel git curl qt5-qtsvg-devel kernel-devel glew-devel
:::


(cloning-repositories)=

## Cloning Repositories

To clone the Open Chemistry repository that
contains the other projects as submodules,

```shell
git clone --recursive https://github.com/OpenChemistry/openchemistry.git
```

Or if you have a GitHub account with SSH key (e.g., for contributing 
changes):

```shell
git clone --recursive git@github.com:OpenChemistry/openchemistry.git
```

## Updating

In order to update the repository from the openchemistry module you can
run,

```shell
git pull
git submodule update --init
```

## Prerequisites

The Open Chemistry projects have a number of prerequisites, and these
vary by platform. On Windows Visual Studio 2017 is best supported. The
superbuild will attempt to build a number of dependencies, on Linux you
are likely best off installing these with your package manager, and on
macOS the homebrew package manager works well.

We should add a package listing for various Linux distributions, but as
a guide you will need:

- a C/C++ compiler that supports C++17
- OpenGL
- Qt 5.6+
- CMake
- Python


```

## Building

It is recommended that you create a build tree outside of the source
tree. Assuming you are in the directory where you cloned the repository
the following commands will create a build tree, configure it and build.

```shell
mkdir openchemistry-build
cd openchemistry-build
cmake ../openchemistry
cmake --build . --config Release
```

You may wish to run cmake-gui in the build directory once it has been
configured. You can build against system libraries to avoid building
them (examples include Boost, Eigen, etc), and turn testing on globally
(ENABLE_TESTS) if you would like to ensure all tests are configured and
built for sub-projects. The --config argument to cmake --build is only
used on the Windows platform with MSVC, and can be removed elsewhere.

(finding-qt-windows-generators)=

### Finding Qt, Windows Generators

We go to great care to use Qt5_DIR as the base for all Qt 5 modules, so
setting the correct Qt5_DIR should result in a valid tree, you can also
use CMAKE_PREFIX_PATH to point at the install prefix of Qt. When setting
Qt5_DIR for Windows, using Qt 5.10.1 as an example, you should set the
variable to 'C:/Qt/Qt5.10.1/5.10.1/msvc2017_64/lib/cmake/Qt5' (without
the quotes). As you upgrade, you can usually just replace the version
(that occurs twice), you must also be careful to match the CMake
generator to the compiler and architecture on Windows, I recommend
'Visual Studio 15 2017 Win64', we no longer build/test 32 bit binaries
on any platform.

(normal-development)=

### Normal Development

You can also open the top-level CMakeLists.txt in Qt Creator, choose the
build location, have that configure and build and then open the
top-level CMakeLists.txt for each of the sub-projects. When setting the
build location choose the openchemistry-build/avogadrolibs for Avogadro,
openchemistry-build/molequeue for MoleQueue, etc. Once you have compiled
the top-level, for normal day-to-day development you are free to ignore
it and perform the majority of work in the project being developed.

(build-tree-layout)=

## Build Tree Layout

The build tree mirrors the source tree for most active projects. So
avogadrolibs is in the same relative path in the source and build trees.
For things such as Boost which are built from a source tarball they can
be found only in the build tree, and are under thirdparty/boost-prefix,
these projects are dependencies but are not expected to be edited in
place.

There is a prefix directory in the base of the build tree. This acts as
an install prefix for all projects, with the normal include, bin, share
and lib directories. This can be used to inject an additional prefix in
CMAKE_PREFIX_PATH to ensure projects build by the superbuild are found.
It keeps the sub-projects relatively simple as they either find stuff in
the prefix, or normal system paths.

(running-executables)=

### Running Executables

It is recommended that you run the binaries from within the prefix
directory in the build tree. The top-level targets (avogadroapp,
molequeue, monogochem) all install to the prefix, if running make from
within the individual build trees run make install to ensure you are
using the latest version. On Linux and Windows running Avogadro 2 looks
like,

```shell
./openchemistry-build/prefix/bin/avogadro2
```

On Mac, it might be:

```shell
open /Users/your-user/openchemistry-build/avogadroapp/bin/Avogadro2.app
```

Note that on Mac with Apple Silicon, you must sign all binaries before opening:
```shell
codesign --force --deep -s "Developer ID Application: Username (Team ID)" prefix/Avogadro2.app
```

(building-packages)=

### Building Packages

The molequeue and avogadroapps projects can build installers.
In order to do this you must cd into the appropriate subdirectory and
call make package. So to build the Avogadro 2 package,

```shell
cd avogadroapp
make package
```

You may need to run cmake-gui, toggle advanced variables and
enable/disable packages you are interested in. They are prefixed by
CPACK, and can be toggled before calling make package. A binary
installer will be created in the build directory.
