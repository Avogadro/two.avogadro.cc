(install-flatpak)=

# Flatpak

[Flatpak](https://flatpak.org/) is an app packaging solution for Linux that solves the issue of differences between distributions and allows a single app to run on all Linux desktops.
This means not just different distros but also both older and newer distros, so if you were stuck using an old version of Avogadro until now, give the flatpak a try.

The Avogadro team is aiming for flatpak to become the primary method of distribution of Avogadro 2 on Linux.
(Though distribution via other routes will of course continue.)

As well as the usual benefits of flatpaks such as stability and the possibility for sandboxing, by using the Avogadro flatpak you can easily keep it up-to-date with the latest versions via updates.

If you've never used flatpak before, the first step is to make sure you have the `flatpak` package, but you likely already do -- it is installed by default on most modern distros.

Avogadro is distributed through [Flathub](https://flathub.org/apps/org.openchemistry.Avogadro2) on two branches: a [`stable`](install-flatpak-stable) branch, which contains the most recent release, and a [`beta`](install-flatpak-beta) branch, which is similar to the "nightly" versions on other platforms and has the latest features and bug fixes.


(install-flatpak-stable)=

## Stable

In many cases, flatpak is set up with Flathub out-of-the-box.
If not, and you haven't set it up yourself manually before, you can follow the instructions [here](https://flathub.org/setup).

Once flatpak is set up, you can easily install Avogadro from Flathub in one of two ways:

1. Through your distro's "app store" (e.g. KDE Discover or GNOME Software) -- just search for Avogadro, or click on install on the [Flathub page](https://flathub.org/apps/org.openchemistry.Avogadro2)
2. On the command line using:
```shell
flatpak install org.openchemistry.Avogadro2
```

After installation, Avogadro should show up in your applications menu/drawer like any other app.
If not, you can always run a flatpak using:
```shell
flatpak run org.openchemistry.Avogadro2
```

:::{tip}
By default, `flatpak` works on the system installation (see the [flatpak usage guide](https://docs.flatpak.org/en/latest/using-flatpak.html)), just like `apt`, `dnf` and friends.
This means that to add repos and install Avogadro using the commands above, or using your distro's software manager, you may need `sudo` privileges.

On the whole it is recommended to do things this way, but it might not always be possible.
To do things just for your user without `sudo` privileges, use the `flatpak` command with the `--user` flag, e.g.
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
While it is possible, it is strongly recommended that you do not have both the `stable` and `beta` version of Avogadro installed at the same time, to avoid complications.
:::

To get the `beta` branch, you will first have to add the `flathub-beta` repository, which is located at `https://flathub.org/beta-repo/flathub-beta.flatpakrepo`.

On the command line this is done using:
```
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
```

If using a GUI software manager to manage your flatpaks, they often also provide a way to add a repository.

Once the repo has been added, you can install the Avogadro `beta` flatpak in the usual way, done on the command line using:
```shell
flatpak install org.openchemistry.Avogadro2//beta
```

The flatpak can then be run in the usual way.

```{toctree}
```
