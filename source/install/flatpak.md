(install-flatpak)=

# Flatpak

On Linux, Avogadro 2 is not only available from [the repositories of many distros](https://repology.org/project/avogadro2/versions), thanks to the work of many dedicated maintainers, and as a stand-alone AppImage, but also in the form of a Flatpak.

The Flatpak provides the best and most reliable Avogadro user experience on Linux, and the Avogadro team recommends using it.

At the same time, the Flatpak does have a couple of limitations (see below) in comparison to other formats, and there are no plans to discontinue any of the other distribution methods, which may suit certain use-cases better.

[Flatpak](https://flatpak.org/) is an app packaging solution for Linux that solves the issue of differences between distributions and allows a single app to run on all Linux desktops.
This means not just different distros but also both older and newer distros -- especially useful if your distro only provides an old version of Avogadro.

As well as the usual benefits of Flatpaks (e.g. stability, sandboxing), by using the Avogadro Flatpak you can easily keep it up-to-date with the latest versions via updates.

If you've never used Flatpak before, the first step is to make sure you have the `flatpak` package, but you likely already do -- it is installed by default on most modern distros.

Avogadro is distributed through [Flathub](https://flathub.org/apps/org.openchemistry.Avogadro2) on two branches: a [`stable`](install-flatpak-stable) branch, which contains the most recent release, and a [`beta`](install-flatpak-beta) branch, which is similar to the "nightly" versions on other platforms and has the latest features and bug fixes.


(install-flatpak-stable)=

## Stable

In many cases, `flatpak` is set up with Flathub out-of-the-box.
If not, and you haven't set it up yourself manually before, you can follow the instructions [here](https://flathub.org/setup).

Once `flatpak` is set up, you can easily install Avogadro from Flathub in one of two ways:

1. Through your distro's "app store" (e.g. KDE Discover or GNOME Software) -- just search for Avogadro, or click on install on the [Flathub page](https://flathub.org/apps/org.openchemistry.Avogadro2)
2. On the command line using:
```shell
flatpak install org.openchemistry.Avogadro2
```

After installation, Avogadro should show up in your applications menu/drawer like any other app.
If not, you can always run a Flatpak from the CLI using:
```shell
flatpak run org.openchemistry.Avogadro2
```

:::{tip}
By default, `flatpak` works on the system installation (see the [flatpak usage guide](https://docs.flatpak.org/en/latest/using-flatpak.html)), just like `apt`, `dnf` and friends.
This means that to add repos and install Avogadro using the commands above, or using your distro's software manager, elevated privileges may be required.

It is generally _not_ recommended to run `flatpak` using `sudo`.
Instead, use the commands as given, and authenticate via PolKit when prompted.

On the whole it is recommended to perform system installation like this, but it might not always be possible.
To install Avogadro just for your user, without elevated privileges, use the `flatpak` command with the `--user` flag, e.g.
```shell
flatpak --user install org.openchemistry.Avogadro2
flatpak --user run org.openchemistry.Avogadro2
```
:::


(install-flatpak-beta)=

## Beta

Though our nightly builds are generally pretty robust, it is not allowed to distribute nightly, potentially unstable builds over Flathub, so instead we are providing an "almost-nightly" `beta` branch to fulfil the same purpose.
It will receive the latest updates at regular intervals.

:::{warning}
While possible, it is strongly recommended that you do _not_ have both the `stable` and `beta` version of Avogadro installed at the same time.
This avoids complications that may arise from the fact that data and configuration files are shared between both.
:::

To get the `beta` branch, you will first have to add the `flathub-beta` repository, which is located at `https://flathub.org/beta-repo/flathub-beta.flatpakrepo`.

On the command line this is done using:
```
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
```

If using a GUI software manager to manage your Flatpaks, they often also provide a way to add a repository.

Once the repo has been added, you can install the Avogadro `beta` Flatpak in the usual way, done on the command line using:
```shell
flatpak install org.openchemistry.Avogadro2//beta
```

The Flatpak can then be run in the usual way.


(install-flatpak-limitations)=

## Limitations

As mentioned, the Flatpak form of Avogadro is generally the version that provides the most robust experience.
However, it is worth mentioning a couple of the downsides.
Some of these are intrinsic to the Flatpak distribution method itself, while others are current problems specific to Avogadro that will be resolved in future.

### Inherent disadvantages of Flatpak

The biggest complaint about Flatpaks is the storage space requirements.
This arises from Flatpak's use of runtimes: extra Flatpak versions of application support libraries that would on Linux normally be provided by the system.
Flatpak runtimes are what allows the same application to run on many different distros, by guaranteeing the same version of the library dependencies.

Runtimes are shared between Flatpak applications, so the effect is most significant and noticeable when either no or very few other Flatpak apps are installed.
As such, if you install the Avogadro Flatpak, you may find that not only Avogadro itself will be downloaded and installed (as of v1.102.0, a modest 78.6 MB download and 166.4 MB installation size) but also a large (~1 GB) KDE runtime.
It is important to realise that this extra storage cost is not paid for every Flatpak application, but only once for all Flatpaks that share the same runtime.

For most users, this amount of storage space is not a concern, and the stability and portability advantages that result are generally worth it.
However, those users for whom storage capacity is tight may be better off sticking to distro packages (requiring <100 MB total) or the AppImage (127 MB as of v1.102.0).

### Current known limitations of the Avogadro Flatpak

By default, Avogadro has no access to your system files when run as a Flatpak.

This is in accordance with best practice and does not generally cause problems, as normal filesystem operations such as opening and saving files are handled by a file dialog that _does_ have access using a "Desktop Portal".
The Flatpak is also provided with a small corner specially reserved for the application's own data, so plugins also work without issue.

As of 2025, however, this sandboxing does cause two known issues, both of which are minor:

#### Drag-and-drop

When a file in some chemical format is dragged onto Avogadro's main window, the usual behaviour is that the file is opened and its contents displayed.

Unfortunately, the Qt library that Avogadro is built on does not yet use a Desktop Portal for this, so it requires the application to have access to the location of the file.
As the Flatpak does not normally have this, drag-and-drop does not work.

The normal functionality is easy to restore, simply by affording the Avogadro Flatpak permission to access the relevant part of your filesystem.

On KDE, this can be done in **System Settings** under **Application Permissions > Avogadro > Manage Flatpak Settings**.
On GNOME and other desktop environments that do not have an in-built way to adjust Flatpak permissions, this can be done most easily using [Flatseal](https://flathub.org/en/apps/com.github.tchx84.Flatseal).
Permissions can also be set via the `flatpak` CLI.

Support for the drag-and-drop Desktop Portal is expected in Qt in the near future, which will solve the issue without requiring applications to have filesystem access.

#### User-specified Python interpreters and environments

Plugins for Avogadro are mostly written in Python and are run behind-the-scenes using a Python interpreter.
In other versions of Avogadro, it is possible to ask Avogadro to use a specific Python interpreter, and therefore also to use the associated virtual environment, allowing users to reuse already-installed versions of large Python packages if they wish.

The way filesystems are handled means that this does not work in the Flatpak version of Avogadro.

Note that Python plugins work with the Flatpak without any problems!
The Avogadro Flatpak includes a Python interpreter, as well as Pixi, which Avogadro uses to maintain its own Python environments and run plugins within the sandbox.
The only functionality that does not work is the custom interpreter setting.

```{toctree}
```
