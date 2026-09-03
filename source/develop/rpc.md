(develop-rpc)=

# Avogadro Remote Procedure Call (RPC)

Avogadro 2 listens on a local socket and accepts [JSON-RPC
2.0](https://en.wikipedia.org/wiki/JSON-RPC) messages, so another program on
the same machine can drive it: open files, load molecules straight from memory,
change the display, render surfaces, animate vibrations, and save images.
MoleQueue and XtalOpt use this to push results into Avogadro for visualization,
and it is a convenient way to script figure generation from Python.

The easiest way to send messages is the `connect` class in the
[avogadro](https://pypi.org/project/avogadro/) package on PyPI. Everything it
does can also be done by writing the JSON packets yourself, which is described
further down.

## Quick start with Python

```sh
pip install avogadro
```

Start Avogadro, then from any Python script or notebook:

```python
from avogadro.connect import connect

with connect() as avo:
    avo.open_file("/path/to/caffeine.cml")
    # render the van der Waals surface
    avo.command("renderVanDerWaals")
    avo.save_graphic("/path/to/caffeine.png")
```

Creating a `connect` object raises `ConnectionError` if Avogadro is not
running. Each call blocks until Avogadro answers, and raises
`avogadro.connect.RPCError` if Avogadro reports a problem:

```python
from avogadro.connect import connect, RPCError

with connect() as avo:
    try:
        avo.command("renderMO", orbital="homo", isovalue=0.02)
    except RPCError as error:
        print(error.code, error.message)
```

### Methods on `connect`

| Method | Description |
|--------|-------------|
| `open_file(filename)` | Open a file from disk, inferring the format from the extension |
| `load_molecule(content, format="cjson")` | Load molecular data from a string |
| `export_file(filename)` | Write the active molecule, inferring the format from the extension |
| `save_graphic(filename)` | Save a bitmap image of the current view |
| `command(name, **options)` | Run any registered command, e.g. `command("setVibrationalMode", mode=3)` |
| `send(method, params=None, wait=True)` | Send any JSON-RPC method; the general escape hatch |
| `ping()` | Return `True` if Avogadro answered |
| `kill()` | Ask Avogadro to quit (only honored with `--testing`, see below) |
| `close()` | Close the connection (also done by the `with` block) |

`command()` and `send()` reach *every* method Avogadro understands, including
commands added by plugins, so the list below is the real vocabulary rather than
the handful of named convenience methods.

Molecules can be sent without touching the disk, which is useful when the data
was generated in the same script:

```python
xyz = """3

O   0.000   0.000   0.119
H   0.000   0.763  -0.477
H   0.000  -0.763  -0.477
"""

with connect() as avo:
    avo.load_molecule(xyz, "xyz")
```

## The connection

Avogadro creates a single local server named `avogadro` when it starts:

* **Linux, macOS, BSD** — a Unix domain socket at `$TMPDIR/avogadro`
  (Python's `tempfile.gettempdir()` resolves to the same place).
* **Windows** — a named pipe at `\\.\pipe\avogadro`.

Only one instance can own the name. When a second copy of Avogadro starts it
sends `internalPing` to the existing server; if it gets a reply the new
instance leaves the server alone, and if it does not it takes the name over.
This means messages always go to the instance that started first and is still
alive.

Each packet on the wire is a 4-byte big-endian unsigned length followed by that
many bytes of UTF-8 JSON. The same framing is used in both directions, so a
reply must be read by taking the 4-byte header first and then exactly that many
bytes.

## Protocol

Requests follow JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "openFile",
  "params": { "fileName": "rutile.POSCAR" }
}
```

`id` is any unique number for that request; the reply carries the same `id`.
`params` is an object whose keys are the options for that method — Avogadro
converts it to a `QVariantMap` before handing it to the plugin, so numbers,
strings, booleans, and lists all pass through.

A successful reply looks like:

```json
{ "jsonrpc": "2.0", "id": 1, "result": true }
```

and a failure like:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": { "code": -32601, "message": "Method not found" }
}
```

Error code `-32601` means the method name is not registered — the original
request is echoed back in `error.data.request`. Code `-1` is used for a
method that exists but could not be carried out, for example a file that
could not be read, or any request that arrives with no Avogadro window open.

:::{note}
`params` is a single JSON object. Older versions of this page showed a nested
form with braces around each key, which is not valid JSON and is not what
Avogadro parses.
:::

## Built-in methods

These are handled by the application itself.

| Method | Parameters | Description |
|--------|-----------|-------------|
| `openFile` | `fileName` | Read a file from disk and make it the active molecule. The format is inferred from the extension (e.g. `POSCAR`, `cml`, `xyz`). |
| `loadMolecule` | `content`, `format` | Read molecular data from a string in any format Avogadro can read, and make it the active molecule. |
| `exportFile` | `fileName` | Write the active molecule. The format is inferred from the extension, and the write is queued asynchronously, so `true` means "started", not "finished". |
| `saveGraphic` | `fileName` | Save a bitmap image of the active view at its current on-screen size. `.png` is appended if the name has no extension. |
| `setProjection` | `type`, or `perspective` / `orthographic` | Switch the camera projection. Either `{"type": "perspective"}` or a bare `{"orthographic": true}` key works. |
| `setRenderTypes` | `types`, or one key per type | Choose which display types are active — see below. |
| `internalPing` | none | Answers `"pong"`. Handled by the RPC layer itself, so it works even before a window exists. |
| `kill` | none | Quit Avogadro. Refused unless Avogadro was started with `--testing`, so that test suites can shut it down without giving every script that power. |

### Display types

`setRenderTypes` takes either a list of names:

```json
{ "method": "setRenderTypes", "params": { "types": ["BallStick", "VanDerWaals"] } }
```

or a set of names mapped to booleans, which also lets you turn types off:

```json
{ "method": "setRenderTypes",
  "params": { "BallStick": true, "Wireframe": false } }
```

A name matches either a plugin's identifier or its translated display name.
Prefer the identifier — it does not change with the interface language:

`BallStick`, `Cartoons`, `CloseContacts`, `CrystalScene`, `Dipole`, `Force`,
`Label`, `Licorice`, `NonCovalent`, `OverlayAxes`, `QTAIMScenePlugin`,
`SurfaceRender`, `SymmetryScene`, `VanDerWaals`, `Wireframe`

## Plugin commands

Tools and extensions register their own commands at startup, and any of them
can be sent as a JSON-RPC method name. Commands that belong to a tool
temporarily make that tool active, run, and then restore the tool you were
using.

Unless noted otherwise, a command needs an open molecule and returns an error
if there is none.

### Atoms and bonds

| Command | Parameters | Description |
|---------|-----------|-------------|
| `createBonds` | none | Perceive bonds between all atoms, or within the selection if there is one. |
| `removeBonds` | none | Remove bonds from all atoms, or from the selection. |
| `addBondOrders` | none | Perceive bond orders. |
| `centerAtom` | `index` (or `id`) | Move the molecule so that this atom sits at the origin. Atoms are numbered from zero. |
| `alignAtom` | `index` (or `id`), `axis` | Rotate the molecule so this atom lies along an axis. `axis` may be `"x"`, `"y"`, `"z"` or `0`, `1`, `2`. |

### Camera and view

| Command | Parameters | Description |
|---------|-----------|-------------|
| `rotateScene` | `x`, `y`, `z` | Rotate the camera about the screen x, y, and z axes, through the current focal point. |
| `zoomScene` | `delta` | Zoom in or out. Positive values move toward the molecule. |
| `translateScene` | `x`, `y` | Pan the camera by a distance given in screen pixels. |
| `alignView` | none | Align the view to the x, y, and z axes, centered on the molecule and backed off far enough to frame it. |

### Crystals

| Command | Parameters | Description |
|---------|-----------|-------------|
| `wrapUnitCell` | none | Wrap all atoms back into the unit cell. |
| `standardCrystalOrientation` | none | Rotate the unit cell into the standard orientation. |
| `fillUnitCell` | none | Add the symmetry-equivalent atoms implied by the space group. |
| `fillTranslationalCell` | none | Fill the cell including atoms related by translation. |

### Surfaces and orbitals

| Command | Parameters | Description |
|---------|-----------|-------------|
| `renderVanDerWaals` (or `renderVDW`) | `resolution` | van der Waals surface. |
| `renderSolventAccessible` | `resolution` | Solvent-accessible surface. |
| `renderSolventExcluded` | `resolution` | Solvent-excluded surface. |
| `renderMO` (or `renderOrbital`) | `orbital`, `isovalue`, `resolution`, `spin` | Molecular orbital, for a file that includes a basis set. |
| `renderElectronDensity` | `isovalue`, `resolution`, `spin` | Total electron density. |
| `renderSpinDensity` | `isovalue`, `resolution`, `spin` | Spin density. |

Shared options:

* `orbital` — either a number, counting from one so that `1` is the lowest
  orbital, or a string relative to the frontier orbitals: `"homo"`, `"lumo"`,
  `"homo-1"`, `"lumo+2"`, and so on.
* `isovalue` — the isosurface value, default `0.03`.
* `resolution` — the cube spacing in Å. If it is left out, Avogadro picks a
  value from the size of the molecule, between 0.05 and 0.5 Å.
* `spin` — set to `"beta"` for the beta orbitals or density of an
  open-shell calculation; alpha is used otherwise.

Surface generation runs in the background. The reply comes back as soon as the
calculation has been started, not when the surface appears.

```python
with connect() as avo:
    avo.open_file("acetone.out")
    avo.command("renderMO", orbital="lumo", isovalue=0.02, resolution=0.1)
```

### Vibrations

| Command | Parameters | Description |
|---------|-----------|-------------|
| `showVibrations` | none | Open the vibrational modes dialog. |
| `setVibrationalMode` | `mode` | Select a mode, numbered from zero. |
| `setVibrationalAmplitude` | `amplitude` | Set the animation amplitude on the same 0–99 scale as the dialog slider, which starts at 20. |
| `startVibrationAnimation` | none | Start animating the selected mode. |
| `stopVibrationAnimation` | none | Stop the animation. |
| `generateDisplacedCoordinates` | `modes` (or `mode`), `scale`, `structures` | Append coordinate sets displaced along one or more modes. `modes` is a list of mode numbers, `scale` defaults to 1.0, and `structures` (default 1) is how many displaced geometries to generate. |

## Adding commands from a plugin

Any `ExtensionPlugin` or `ToolPlugin` can add to this vocabulary. Register the
names in `registerCommands()` and act on them in `handleCommand()`:

```cpp
void MyExtension::registerCommands()
{
  emit registerCommand("renderMovie", tr("Render a movie of the current view."));
}

bool MyExtension::handleCommand(const QString& command,
                                const QVariantMap& options)
{
  if (command == "renderMovie") {
    renderMovie(options.value("fileName").toString());
    return true;
  }
  return false; // becomes a "Method not found" error
}
```

The application collects these at startup, so a command is available as soon as
the plugin loads. Return `false` for anything you do not handle — including a
command of yours that was sent with options it cannot use — so that the caller
gets an error rather than a silent success. If the work continues after
`handleCommand()` returns, emit `commandFinished()` when it is done.

## Writing the packets directly

If you would rather not depend on the Python package, the protocol is small
enough to implement anywhere. In Python it is about a dozen lines:

```python
import json
import socket
import struct
import tempfile

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect(tempfile.gettempdir() + "/avogadro")

request = json.dumps({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "openFile",
    "params": {"fileName": "rutile.POSCAR"},
}).encode("utf-8")
sock.sendall(struct.pack(">I", len(request)) + request)

size = struct.unpack(">I", sock.recv(4))[0]
print(json.loads(sock.recv(size).decode("utf-8")))
```

On Windows, open `\\.\pipe\avogadro` as an unbuffered binary file instead of
creating a socket; the framing and the JSON are identical.
