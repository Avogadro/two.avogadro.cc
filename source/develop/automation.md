(develop-automation)=

# Automation and Headless Usage

Avogadro can be driven entirely by a script: start it, send it
[RPC commands](develop-rpc), let it compute surfaces and orbitals, save
images and files, then shut it down, with nobody at the keyboard. This page
covers how to do that reliably, including on servers and in CI jobs that have
no display at all.

There is no separate command-line program. Automation uses the normal
Avogadro application, controlled over its JSON-RPC socket, usually with the
`connect` class from the [avogadro](https://pypi.org/project/avogadro/)
Python package. A script typically:

1. launches Avogadro with its own socket name,
2. waits until Avogadro answers,
3. sends commands, waiting for the slow ones to finish,
4. renders images or exports files, and
5. stops the Avogadro process.

:::{note}
This page describes Avogadro 2.1. `--rpc-name`, waiting for commands to
finish, and `renderImage` are not available in earlier versions. Use the
`avogadro` Python package that matches your Avogadro version.
:::

## Launching Avogadro for scripting

The executable is `avogadro2` on Linux, `avogadro2.exe` on Windows, and
`Avogadro2.app/Contents/MacOS/Avogadro2` inside the macOS application
bundle. These options are useful when it is started by a script:

| Option | Effect |
|--------|--------|
| `--rpc-name NAME` | Listen on the socket `NAME` instead of `avogadro`. Also implies `--skip-dialogs`. |
| `--skip-dialogs` | Skip the dialogs that can appear at startup, so that nothing waits for a click. |
| `--disable-settings` | Use default settings and do not save any, so a scripted run neither depends on nor changes your preferences. |
| `--skip-autosave` | Do not restore or write autosave files. |
| `FILE ...` | Open these files at startup. |

A typical launch line is:

```sh
avogadro2 --rpc-name avo-batch --disable-settings --skip-autosave
```

Give every scripted instance its own `--rpc-name`. Only one running
Avogadro can own a socket name, and the default name `avogadro` belongs to
whichever copy was started first, which may be the one you are using
interactively. With a separate name, a script can run alongside your normal
session, and several scripts can run at once. Including the process ID in the
name is an easy way to keep it unique.

On Linux, macOS and BSD the socket is created in the system temporary
directory (Python's `tempfile.gettempdir()`); on Windows it is the named pipe
`\\.\pipe\NAME`. macOS limits socket paths to 104 bytes, and its temporary
directory is already long, so keep names short.

## Waiting for Avogadro to start

Avogadro takes a moment to start, and the socket does not exist until it has.
Even once the socket answers, most methods return an error until the main
window is ready. A simple approach is to retry `molecule_info()`, which only
succeeds once the window exists:

```python
import os
import subprocess
import time

from avogadro.connect import connect, RPCError

AVOGADRO = "avogadro2"


def start_avogadro(name, timeout=60):
    """Launch Avogadro listening on `name` and wait until it is ready."""
    process = subprocess.Popen(
        [AVOGADRO, "--rpc-name", name, "--disable-settings", "--skip-autosave"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError(
                "Avogadro exited during startup (code %d)" % process.returncode
            )
        try:
            with connect(name, timeout=5) as avo:
                avo.molecule_info()  # fails until the main window exists
            return process
        except (OSError, RPCError):  # not listening yet, or no window yet
            time.sleep(0.5)
    stop_avogadro(process)
    raise TimeoutError("Avogadro did not start within %d s" % timeout)


def stop_avogadro(process):
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()
```

Requests that read or write files (`openFile`, `loadMolecule`, `exportFile`,
`getMolecule`) are held for a second or two after startup, until the file
formats provided by plugins such as Open Babel have loaded. You do not need to
wait for that yourself.

(automation-wait)=

## Waiting for commands to finish

Some commands return as soon as their work has *started*: computing a
surface or orbital runs on a background thread, and `exportFile` writes the
file on one. Saving an image straight after starting a surface would capture
the view before the surface exists.

Pass `wait=True` (and optionally a `timeout` in seconds, 60 by default) and
Avogadro holds its reply until the command has really finished:

```python
avo.command("renderMO", orbital="homo", isovalue=0.02, wait=True, timeout=300)
```

`export_file()`, `fetch_by_name()` and `fetch_pdb()` wait by default. For
other commands, `wait=True` is harmless when the command finishes straight
away, so it is a safe default in scripts. A command that fails or runs out of
time raises `RPCError` with code `-2`. A command sent while the same plugin
is still busy raises `RPCError` with code `-3`.

Large grids are slow, especially without a GPU. Raise `timeout` for big
molecules or a fine `resolution`, rather than letting the request fail.

## Rendering images

`render_image()` renders the active view to a PNG. It can write a file or
return the PNG bytes directly:

```python
avo.render_image(width=1600, height=1200, filename="/data/homo.png")

png_bytes = avo.render_image(transparent=True)  # nothing written to disk
```

* Leave out `width` and `height` for the view's own resolution, or give both
  (each up to 8192 pixels).
* `transparent=True` keeps the background transparent.
* The image is rendered at the size of the view in the Avogadro window and
  then scaled to the requested size. If the requested shape is different from
  the view's, the image is centered on a padded canvas rather than reframed,
  so the molecule sits smaller in the picture. Match the aspect ratio of the
  window, or make the window larger (see [Running without a
  display](automation-headless)), for the best results.

`save_graphic(filename)` also works, but always saves at the window's current
size.

The rest of the view can be set before rendering:

```python
avo.set_display_types({"BallStick": True, "Wireframe": False})
avo.set_projection("orthographic")

camera = avo.get_camera()  # save a view...
avo.set_camera(model_view=camera["modelView"])  # ...and restore it later
```

`get_camera()` returns plain JSON-friendly data, so a view set up by hand in
Avogadro can be saved once and reused for a whole series of images.

### Paths

File names are read by the Avogadro process, which may have a different
working directory from your script. Use absolute paths for `open_file()`,
`export_file()`, `render_image()` and `save_graphic()`.

## Avoiding dialogs

A modal dialog stops a script: Avogadro still answers `ping()` and other
connections, but the request that opened the dialog never gets a reply.
`--rpc-name` turns on `--skip-dialogs`, and with it a failed `exportFile` or
`saveGraphic` returns an error instead of opening a message box. Some
commands can still open a dialog, so avoid these in unattended scripts:

* `showPdfPlot` and `showXrdPlot`, which ask for their options in a modal
  dialog
* other commands whose names start with `show`, such as `showVibrations`,
  which open windows
* `fetchPDB` and `fetchByName`, which also depend on the network

If a script seems stuck, a second connection can ask what is open:

```python
with connect("avo-batch") as probe:
    print(probe.send("activeDialog")["result"])  # open, title, className
```

## Stopping Avogadro

Stop a scripted Avogadro by ending its process, as `stop_avogadro()` above
does. Anything not yet exported is lost, so call `export_file()` (which waits
for the write to finish) for every result you want to keep. Starting with
`--skip-autosave` means no autosave files are left behind.

:::{note}
The `kill` method is refused unless Avogadro was started with `--testing`,
which current versions do not accept on the command line. Ending the
process is the supported way to stop a scripted instance.
:::

(automation-headless)=

## Running without a display

Avogadro always creates its main window and needs a working OpenGL context,
both for rendering and for a check it makes at startup. On a server, in a
container or in CI with no screen attached, give it a virtual display.

### Linux: Xvfb

[Xvfb](https://www.x.org/releases/current/doc/man/man1/Xvfb.1.xhtml) is an X
server that draws into memory. Together with Mesa's software OpenGL
(llvmpipe) it lets Avogadro run, compute surfaces and render images with no
GPU and no monitor. Avogadro's own end-to-end RPC tests run this way.

On Debian or Ubuntu, install Xvfb, Mesa and the X libraries Qt needs:

```sh
sudo apt-get install xvfb libgl1-mesa-dri libglx-mesa0 libegl1 \
  libxkbcommon-x11-0 libxcb-cursor0 libxcb-icccm4 libxcb-image0 \
  libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 \
  libxcb-xinerama0 libxcb-xkb1
```

Then run your script (which launches Avogadro) under `xvfb-run`:

```sh
export LIBGL_ALWAYS_SOFTWARE=1   # use Mesa's software renderer
export QT_QPA_PLATFORM=xcb       # use X11, even if Wayland is configured
xvfb-run -a -s "-screen 0 1920x1080x24" python render_orbitals.py
```

`-a` picks a free display number, so several jobs can run on one machine.
The screen size limits how large the Avogadro window, and therefore the
native render size, can be.

For a long-running service, start one Xvfb server and point everything at it
instead:

```sh
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
```

Avogadro asks for OpenGL 4.0 (core profile). Older Mesa releases do not
provide that in software. To check what you have:

```sh
xvfb-run -a glxinfo -B   # from the mesa-utils package
```

and look for an `OpenGL core profile version string` of 4.0 or higher. If
Avogadro cannot get a usable context it prints
`This system does not support OpenGL.` and exits.

:::{note}
Setting `QT_QPA_PLATFORM=offscreen` *without* an X server is not a
substitute. It is fine for code that never draws, but Avogadro needs a real
OpenGL context and will not start reliably that way. Use Xvfb.
:::

Software rendering is slower than a GPU, but the slow part of most scripts
is computing orbital and surface grids, which runs on the CPU either way.

Prefer a native build or the AppImage for automation. Flatpak keeps
applications in a sandbox with their own temporary directory, so a script
running outside the sandbox may not be able to see the socket.

### macOS and Windows

There is no equivalent of Xvfb. Avogadro needs a logged-in desktop session:

* **macOS** — run under a user who is logged in at the console (or through
  Screen Sharing). A plain SSH login with nobody logged in cannot open
  windows.
* **Windows** — run in an interactive desktop session, not as a service.

The window can stay in the background or be minimized while the script runs.

## A complete example

This script renders the HOMO and LUMO of every `.fchk` file in a directory.
Run it under `xvfb-run` on a machine without a display.

```python
import os
import sys
from pathlib import Path

from avogadro.connect import connect

# start_avogadro() and stop_avogadro() as defined above

name = "avo-%d" % os.getpid()
folder = Path(sys.argv[1]).resolve()

process = start_avogadro(name)
try:
    with connect(name) as avo:
        avo.set_display_types({"BallStick": True})
        for path in sorted(folder.glob("*.fchk")):
            avo.open_file(path)
            if avo.molecule_info()["hasBasisSet"]:
                for orbital in ("homo", "lumo"):
                    avo.command(
                        "renderMO",
                        orbital=orbital,
                        isovalue=0.02,
                        wait=True,
                        timeout=300,
                    )
                    image = path.with_name(f"{path.stem}-{orbital}.png")
                    avo.render_image(width=1600, height=1200, filename=image)
            # Close each molecule so they do not pile up in memory.
            avo.send("closeMolecule", {"discard": True})
finally:
    stop_avogadro(process)
```

`avo.list_commands()` lists every command the running Avogadro understands,
including those added by plugins. See [RPC](develop-rpc) for the full
protocol and the options of each command.
