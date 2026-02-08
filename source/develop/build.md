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

The instructions in this guide assume that you know how to execute commands in a terminal.

:::{tip}
Platform-specific instructions, guidance, and information is provided in expandable callouts marked by the respective icons {fab}`windows` {fab}`apple` {fab}`linux`.
:::

:::{admonition} Windows {fab}`windows`
:class: dropdown
For steps that require using the command line in a terminal, we recommend using Powershell 7 within Microsoft Terminal, which should be installed on your system already if you are using Windows 11 -- if not, you can get it from the [Microsoft Store](https://apps.microsoft.com/detail/9n0dx20hk701?ocid=webpdpshare).

In recent versions of Powershell, Linux/macOS commands like `cd` are aliased to their Powershell equivalents, so all of the commands that you are instructed to carry out here should work fine.
:::


## System

Only 64-bit operating systems are supported.

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

The Open Chemistry project uses [Git](https://git-scm.com/) for version control, so the first step is to ensure that you have it installed and set up on your system.

### Compiler and build system

:::{tip}
For those unfamiliar with compiling programs from source, or C++ ones in particular, building a modern C++ program typically uses three critical components:
- a compiler, which turns source code files into "object" files containing machine code
- a build tool, which automates the compilation and makes sure all compiler commands are run in the right order
- a build-system generator, which creates configuration files for a build tool based on a set of instructions; this makes building complex projects on multiple platforms with potentially different build tools and compilers much easier
:::

Broadly, you will need a C/C++ compiler that supports C++17, a build tool such as [Ninja](https://ninja-build.org/), and [CMake](https://cmake.org).

:::{admonition} Windows {fab}`windows`
:class: dropdown
On Windows, the MSVC compiler is best supported, which is obtained as part of [Visual Studio](https://visualstudio.microsoft.com/).

If, when installing Qt (see below), you choose to install "Developer and Designer Tools", this will install Ninja and CMake at the same time.
Otherwise, you will need to download and install them separately.

CMake can also be installed using `winget install --exact --id Kitware.CMake`.
:::

:::{admonition} macOS {fab}`apple`
:class: dropdown
We recommend to use [Clang 17](https://clang.llvm.org/) on a Mac, with Ninja and CMake.
:::

:::{admonition} Linux {fab}`linux`
:class: dropdown
Both `gcc`/`g++` and `clang`/`clang++` generally work fine, as do both Unix Makefiles and Ninja.

If you find you have problems compiling, stick to the combination of **gcc with Ninja**; this is what the automatic preparation of Avogadro binaries with GitHub actions uses, so if it is working successfully there, it should also work for you.
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
- `QtOpenGLWidgets`
- `QtConcurrent`
- `QtNetwork`
- `QtSvg`

There are often separate `-devel` versions of each module as well, in which case, you will also need those.
:::


#### Other libraries

##### Necessary

:::{admonition} Windows {fab}`windows`
:class: dropdown
The main other library you will need to get is OpenSSL 3.3.2, either from the [Shining Light Productions website](https://slproweb.com/products/Win32OpenSSL.html) or using `winget install --exact --id ShiningLight.OpenSSL.Dev`
:::


:::{admonition} Linux {fab}`linux`
:class: dropdown

You will need to install the following from your package manager, or similarly named equivalents:

- `glu-devel`
- `libxml2-devel`
- `xz-devel`
- `readline-devel`
- `rapidjson-devel`

You will also need `libopenssl` -- either v1.1 if are building with Qt 5, or >3.0 if you are building with Qt 6.

:::{warning}
For a successful build of Open Babel and therefore a successful build of Avogadro, the `rapidjson` version used cannot be the v1.1.0 release; it must have been patched to include at least [this patch](https://github.com/Tencent/rapidjson/pull/719) from 2016.
Your distro probably distributes a version including this patch, but if you have problems with the Open Babel build step, this may be why.
:::
:::


(system-deps)=
##### Optional

Many dependencies that Avogadro needs will be automatically downloaded and built during the build process.
This means you do not need to install them in advance, and versions will be used that the Avogadro team has determined are compatible.

However, if you would prefer to use versions of these libraries that are installed on your system, you can build Avogadro with CMake flags of the style `-DUSE_SYSTEM_EIGEN`.
For some of them it is also possible to do without them altogether by telling Avogadro to build without the features that require it.

This list includes:

- `glew`
- `eigen`
- `OpenBabel`
- `spglib`
- `libarchive`
- `msgpackc`
- `mmtf-cpp`
- `libmsym`

:::{warning}
If these libraries are not available on your machine, internet access will be required during the build step.

See [Building offline](building-offline) for assistance in circumventing the need for an internet connection.
:::


(cloning-repositories)=

## Getting the source code

All further instructions will assume you are using `git` on the command line.

As mentioned above, by far the easiest way to build Avogadro is to use the Open Chemistry repository as a basis, which contains the other projects as submodules.
Though building each submodule separately is possible, this "superbuild" approach is the only option we explicitly recommend and support.

The submodules of the main repo can be cloned all in one go, or manually for finer control over which ones are downloaded.


### Recursive clone

You can clone the main repo and all submodules automatically using:

```shell
git clone --recursive https://github.com/OpenChemistry/openchemistry.git
git submodule update --init --recursive
```

You can then later easily update all modules at once using:

```shell
git submodule update --remote
```

See the [git submodule documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules) for further help.


### Manual clone

You may prefer to only clone some of the submodules, or you may encounter problems with the recursive clone.
In this case, you are still recommended to clone the main repo, but take the following manual approach instead:

```shell
git clone https://github.com/OpenChemistry/openchemistry.git
cd openchemistry
git clone https://github.com/OpenChemistry/avogadrolibs.git
git clone https://github.com/OpenChemistry/avogadroapp.git
```

This will overwrite each git submodule with a new normal git repository, and can be continued for as many submodules as desired.


#### Required and optional submodules

To build the Avogadro desktop program, only the main Open Chemistry repo and the following submodules are strictly required:

- `avogadrolibs` from https://github.com/OpenChemistry/avogadrolibs.git
- `avogadroapp` from https://github.com/OpenChemistry/avogadroapp.git

The following submodules are optional and add extra functionality to Avogadro:

- `avogadro-i18n`, for languages other than US English, from https://github.com/OpenChemistry/avogadro-i18n.git
- `avogadrogenerators`, for generation of input files for computational packages, from https://github.com/OpenChemistry/avogenerators.git
- `crystals`, `fragments` and `molecules`, which populate the libraries of ready-to-use structures, from https://github.com/OpenChemistry/crystals.git, https://github.com/OpenChemistry/fragments.git, and https://github.com/OpenChemistry/molecules.git
- `avogadrodata`, which contains only a few files for testing, from https://github.com/OpenChemistry/avogadrodata.git
- `molequeue`, which lets you queue computational calculations from Avogadro, but is currently unmaintained, from https://github.com/OpenChemistry/molequeue.git

More information on the contents of each can be found at [Project Structure](develop-structure).


## Building Avogadro

The Open Chemistry project uses CMake to direct builds, so builds are configured and started using the `cmake` command.
This is done in two individual steps.

Again, the following instructions assume you are using the "superbuild" approach.


(configuring-build)=
### Configuring CMake

It is recommended that you create the build tree outside of the source tree.

To set up the build tree, first navigate to the directory containing the cloned `openchemistry` repository, then run the following command:

```shell
cmake -DQT_VERSION=5 -DBUILD_MOLEQUEUE=OFF -S ./openchemistry -B ./build
```

This will create a new directory, `build`, in the current directory next to `openchemistry`, then construct the build tree within it.

To configure the build to build against Qt 6, use `-DQT_VERSION=6` instead.

To use a different compiler (such as `clang` on Linux when the default is `gcc`), add the flags `-DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++`.

To use a different build tool than whatever the default is on your system, add e.g. `-G Ninja`.

:::{admonition} Windows {fab}`windows`
:class: dropdown
On Windows you may need to run with any or all of the following flags, with the paths adjusted as appropriate:

```shell
cmake -DQT_VERSION=5 -DBUILD_MOLEQUEUE=OFF -DQt5_DIR=C:/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5 -DCMAKE_TOOLCHAIN_FILE=C:/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5/Qt5Config.cmake -S ./openchemistry -B ./build
```

or if building against Qt 6:

```shell
cmake -DQT_VERSION=6 -DBUILD_MOLEQUEUE=OFF -DQt6_DIR=C:/Qt/6.8.0/msvc2022_64/lib/cmake/Qt6 -DCMAKE_TOOLCHAIN_FILE=C:/Qt/6.8.0/msvc2022_64/lib/cmake/Qt6/Qt6Config.cmake -DCMAKE_PREFIX_PATH="C:/Qt/6.8.0/msvc2022_64/lib/cmake/Qt6;C:/Qt/6.8.0/msvc2022_64/lib/cmake" -DQT_ADDITIONAL_PACKAGES_PREFIX_PATH=C:/Qt/6.8.0/msvc2022_64 -S ./openchemistry -B ./build
```
:::


(build-types)=
#### Build types

By default, Avogadro will be built in "Debug" mode, which, as the name hints, makes it easier to track down bugs, but at the cost of an increased package size and less optimized (read: slower) code in comparison to "Release" mode.

To change the build type used, use the corresponding flag for `cmake` during the configuration step, e.g.:

```shell
cmake -DQT_VERSION=5 -DBUILD_MOLEQUEUE=OFF -DCMAKE_BUILD_TYPE=Release -S ./openchemistry -B ./build
```

Possible build types for Avogadro are "Debug", "Release", "MinSizeRel" and "RelWithDebInfo".

:::{admonition} Windows {fab}`windows`
:class: dropdown
On Windows the build type cannot be set in this way and must instead be indicated during the [build step](running-build) by e.g.:

```shell
cmake --build ./build --config Release
```
:::


#### Avogadro-specific CMake flags

Avogadro's build process can be configured in a variety of ways by passing extra flags to the above `cmake` command.
In particular this is a good way to add extra functionality or to keep the build slim.
Here is a *non-exhaustive* list of some useful ones, with a short explanation and the default.

```
BUILD_SHARED_LIBS "Build with shared libraries" ON
DOWNLOAD_TO_SOURCE_DIR "Download external dependency source archives to CMAKE_CURRENT_SOURCE_DIR/Downloads" OFF
DOWNLOAD_TO_BINARY_DIR "Download external dependency source archives to CMAKE_CURRENT_BINARY_DIR/Downloads" ON
# If both the above are set to `ON` then the SOURCE directory will be used
# If both the above are set to `OFF` then the user's personal Downloads folder will be used
USE_VTK "Enable libraries that use VTK in Avogadro" OFF
USE_HDF5 "Enable functionality that requires HDF5" OFF
USE_PYTHON "Enable functionality that requires Python" OFF
USE_YAEHMOP "Enable functionality that requires Yaehmop" OFF
USE_SYSTEM_{Dependency} "Use a system installation of {Dependency}" OFF
BUILD_MOLEQUEUE "Build the MoleQueue application" # Default depends on the Qt version
BUILD_AVOGADRO "Build the Avogadro 2 application" ON
BUILD_GPL_PLUGINS "Build GPL plugins, i.e. QTAIM in Avogadro" OFF
BUILD_DOCUMENTATION "Build documentation (Doxygen)" OFF
ENABLE_TESTING "Enable testing for Open Chemistry projects" OFF
```

To use them, prefix them with `-D`.
For example, to build with the VTK functionality and the automatically generated API documentation, you might run:

```shell
cmake -DQT_VERSION=6 -DBUILD_MOLEQUEUE=OFF -DUSE_VTK=ON -DBUILD_DOCUMENTATION=ON -S ./openchemistry -B ./build
```

The following should, when used, also be passed on to `avogadrolibs` to configure its build.
If the desktop application is being built, they are not particularly useful.

```
USE_OPENGL "Enable libraries that use OpenGL" ON
USE_LIBARCHIVE "Enable optional Libarchive features" ON
USE_LIBMSYM "Enable optional features using libmsym" ON
USE_SPGLIB "Enable optional features using spglib" ON
USE_MMTF "Enable optional features using mmtf" ON
```

Likewise, the following should be passed on to `avogadroapp` when given.

```
Avogadro_ENABLE_RPC "Enable RPC server" ON
```

For all available flags, see the `CMakeLists.txt` file in the top level of each project.


(building-offline)=
### Building offline

In some situations it may not be possible or desirable to have the build process download the source code for the third-party dependencies during the build itself.

One way to do this is to download the source code manually in advance and place the **compressed archives** in the *source* directory under `openchemistry/Downloads`.
This needs to be done for all the dependencies listed as [optional dependencies](system-deps).

Then, when running the above `cmake` configure step, pass `-DDOWNLOAD_TO_SOURCE_DIR=ON` as one of the flags.

For this to work, you need to download the exact versions specified in `openchemistry/cmake/projects.cmake`, in the archive format expected.

The alternative is to turn off the use of each of these dependencies (see above for the necessary flags).


(running-build)=
### Starting the build

Once everything is configured, actually building is a simple matter of running:

```shell
cmake --build ./build
```

:::{admonition} Windows {fab}`windows`
:class: dropdown
On Windows you may wish to build a better optimized version of the program by running the build instead with:

```shell
cmake --build ./build --config Release
```

See [Build types](build-types) for more information.
:::

:::{admonition} Linux {fab}`linux`
:class: dropdown
If you used Ninja by passing `-G Ninja` in the configuration step, the build will automatically run in parallel.

If you are using the default GNU Makefiles instead, the build will by default only use a single thread; to run in parallel use:

```shell
cmake --build ./build -j 4
```

where `4` is replaced by the number of threads you wish to use.
This results in significant speed-ups (roughly n times faster in the author's brief tests!).
:::


(build-tree-layout)=
## Layout of the build directory

Each submodule and project will initially be built within its own directories within the build directory, mirroring the source tree.

When using the "superbuild" strategy detailed here, all compiled libraries, objects, and binaries, as well as all supporting resources such as icons and metadata, are additionally installed to the `prefix` directory within the build directory, so that everything can be found in one convenient location.

`prefix` contains the normal `include`, `bin`, `share` and `lib` subdirectories.

:::{tip}
This can be used to inject an additional prefix in `CMAKE_PREFIX_PATH` to ensure that projects built by the superbuild are found by each other.

It keeps the sub-projects relatively simple as they either find stuff in the prefix, or normal system paths.
:::


(running-executables)=
## Running executables

It is recommended that you run the binaries from within the `prefix` directory in the build directory, e.g.:

```shell
./build/prefix/bin/avogadro2
```

or on Windows:

```shell
./build/prefix/bin/avogadro2.exe
```

On Mac on the other hand it might be:

```shell
open /Users/your-user/openchemistry-build/avogadroapp/bin/Avogadro2.app
```

:::{admonition} macOS {fab}`apple`
:class: dropdown
Note that on macOS running on Apple Silicon, you must sign all binaries before opening:

```shell
codesign --force --deep -s "Developer ID Application: Username (Team ID)" prefix/Avogadro2.app
```
:::


(building-installers)=
### Building installers

`avogadroapp` can build installers for Avogadro.

In order to do this, move into the cd into the appropriate subdirectory within the build tree and call `make package`. So, to build the Avogadro 2 package:

```shell
cd build/avogadroapp
make package
```

You may need to run cmake-gui, toggle advanced variables and enable/disable packages you are interested in.
They are prefixed by CPACK, and can be toggled before calling `make package`.
A binary installer will be created in the build directory.
