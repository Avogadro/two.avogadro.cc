(develop-rpc)=

# Avogadro Remote Procedure Call (RPC)

Avogadro 2 listens on a local socket and accepts [JSON-RPC
2.0](https://en.wikipedia.org/wiki/JSON-RPC) messages, so another program on
the same machine can drive it: open files, load molecules straight from memory,
select and edit atoms, run force fields, change the display, render surfaces
and orbitals, animate vibrations, and save images. MoleQueue and XtalOpt use
this to push results into Avogadro for visualization, and it is a convenient
way to script figure generation or whole workflows from Python.

The easiest way to send messages is the `connect` class in the
[avogadro](https://pypi.org/project/avogadro/) package on PyPI. Everything it
does can also be done by writing the JSON packets yourself, which is described
further down.

:::{note}
This page describes Avogadro 2.1. Waiting for commands to finish, read-back
methods such as `moleculeInfo` and `renderImage`, and most of the plugin
commands below are new in 2.1. Use the `avogadro` Python package from the
same release: earlier versions of `avogadro.connect` lack most of the helpers
shown here.
:::

## Quick start with Python

```sh
pip install avogadro
```

Start Avogadro, then from any Python script or notebook:

```python
from avogadro.connect import connect

with connect() as avo:
    avo.open_file("/path/to/caffeine.cml")
    # render the van der Waals surface, and wait until it is ready
    avo.command("renderVanDerWaals", wait=True)
    avo.render_image(width=1200, height=900, filename="/path/to/caffeine.png")
```

Creating a `connect` object raises `ConnectionError` if Avogadro is not
running. Each call blocks until Avogadro answers, and raises
`avogadro.connect.RPCError` if Avogadro reports a problem:

```python
from avogadro.connect import connect, RPCError

with connect() as avo:
    try:
        avo.command("renderMO", orbital="homo", isovalue=0.02, wait=True)
    except RPCError as error:
        print(error.code, error.message)
```

### Getting results back

Many commands report something useful: the atoms now selected, a measured
distance, an energy, whether an optimization converged. That data is only sent
when the request asks to **wait**. Without `wait=True` a plugin command
answers `true` as soon as it has been accepted, which for surfaces, orbitals
and force field calculations is before the work has even finished.

`result_data()` pulls the data out of a waited reply:

```python
from avogadro.connect import connect, result_data

water = """3

O   0.000   0.000   0.119
H   0.000   0.763  -0.477
H   0.000  -0.763  -0.477
"""

with connect() as avo:
    avo.load_molecule(water, "xyz")
    reply = avo.command("measureAngle", atoms=[1, 0, 2], wait=True)
    print(result_data(reply)["angle"])  # about 104

    reply = avo.command("optimize", method="UFF", wait=True, timeout=300)
    data = result_data(reply)
    print(data["energy"], data["unit"], data["converged"])
```

`wait=True` is harmless for a command that finishes straight away, so it is a
sensible default in scripts. See [Waiting for commands to
finish](automation-wait) for timeouts.

### Methods on `connect`

| Method | Description |
|--------|-------------|
| `open_file(filename)` | Open a file from disk, inferring the format from the extension |
| `load_molecule(content, format="cjson")` | Load molecular data from a string |
| `get_molecule(format="cjson")` | Return the active molecule as a string in any format Avogadro can write |
| `export_file(filename, wait=True)` | Write the active molecule, inferring the format from the extension; waits for the write to finish |
| `fetch_by_name(name)` | Download a structure by chemical name and load it |
| `fetch_pdb(code)` | Download a Protein Data Bank entry by its four-character code |
| `molecule_info()` | Summary of the active molecule: counts, formula, charge, whether it has orbitals, vibrations, a unit cell, and so on |
| `render_image(width=None, height=None, transparent=False, filename=None)` | Render the view to a PNG file, or return the PNG bytes |
| `save_graphic(filename)` | Save an image of the view at the window's current size |
| `list_display_types()` / `set_display_types(types)` | List or change the active display types |
| `set_projection(kind)` | `"perspective"` or `"orthographic"` |
| `get_camera()` / `set_camera(model_view=None, projection=None, orthographic_scale=None)` | Read or restore the exact view |
| `version()` | Versions of Avogadro, its libraries, Qt, and the RPC protocol |
| `list_commands()` | Every method this Avogadro understands, including plugin commands |
| `command(name, wait=False, timeout=None, **options)` | Run any command, e.g. `command("setVibrationalMode", mode=3)` |
| `send(method, params=None, wait=False, timeout=None)` | Send any JSON-RPC method; the general escape hatch |
| `ping()` | Return `True` if Avogadro answered |
| `kill()` | Ask Avogadro to quit (refused, see below) |
| `close()` | Close the connection (also done by the `with` block) |

`command()` and `send()` reach *every* method Avogadro understands, including
commands added by plugins, so the lists below are the real vocabulary rather
than the handful of named helpers. The command name is positional-only, so a
command can take an option called `name`, as in
`avo.command("fetchByName", name="caffeine")`. Only `wait` and `timeout` are
reserved.

As the example shows, molecules can be sent without touching the disk, which
is useful when the data was generated in the same script, and read back with
`get_molecule()` in any format Avogadro can write.

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

To use a different name, start Avogadro with `--rpc-name NAME` and pass the
same name to the client, e.g. `connect("NAME")`. This lets a script run its
own copy of Avogadro alongside your regular session. See [Automation and
Headless Usage](develop-automation).

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
`params` is a single JSON object whose keys are the options for that method.
Avogadro converts it to a `QVariantMap` before handing it to the plugin, so
numbers, strings, booleans, and lists all pass through. Atom, bond, layer and
molecule indices count from zero unless a command says otherwise.

Two keys in `params` are reserved and never reach a plugin:

* `wait` — when `true`, hold the reply until the command has finished, and
  include any data it reports.
* `timeout` — how many seconds to wait before giving up, when `wait` is set.
  The default is 60.

### Replies

A successful reply has one of three shapes, depending on the method:

* **Plain** — `"result": true`. This is what every command answers when it was
  sent without `wait`.
* **Read-back** — methods that exist to report something (`version`,
  `moleculeInfo`, `getMolecule`, `renderImage`, `listCommands`,
  `listMolecules`, `listTools`, `listDisplayTypes`, `getCamera`, `setCamera`,
  `activeDialog`) put their answer straight in `result`, with or without
  `wait`:

  ```json
  { "jsonrpc": "2.0", "id": 2,
    "result": { "atomCount": 3, "formula": "H2 O", "hasBasisSet": false } }
  ```

* **Finished** — a command sent with `wait` answers with a `status`, an
  optional human-readable `message`, and any `data` it reports:

  ```json
  { "jsonrpc": "2.0", "id": 3,
    "result": { "status": "finished",
                "data": { "atoms": [1, 0, 2], "angle": 104.5 } } }
  ```

A failure looks like:

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "error": { "code": -2, "message": "There is nothing to undo." }
}
```

| Code | Meaning |
|------|---------|
| `-1` | The request could not be carried out: a file that could not be read or written, a malformed parameter to a method such as `renderImage` or `setCamera`, or no Avogadro window open yet. |
| `-2` | The command ran and failed, or did not finish within `timeout`. The message says why. |
| `-3` | That plugin is still busy with an earlier command. Wait for it, or send the earlier one with `wait`. |
| `-32601` | `Method not found`: no built-in or plugin claims this method. The original request is echoed back in `error.data.request`. |

A few older plugin commands still answer `-32601` instead of `-2` when an
option is missing or invalid; these are noted below.

Requests that read or write molecule files (`openFile`, `loadMolecule`,
`exportFile`, `getMolecule`) are held for a second or two after Avogadro
starts, until the file formats provided by plugins such as Open Babel have
loaded. Later requests queue behind them, so replies always come back in the
order the requests were sent.

## Built-in methods

These are handled by the application itself. Most need a main window, and
answer `-1` while Avogadro is still starting; `version`, `activeDialog`,
`internalPing` and `kill` work before that.

### Files and molecules

| Method | Parameters | Description |
|--------|-----------|-------------|
| `openFile` | `fileName` | Read a file from disk and make it the active molecule. The format is inferred from the extension (e.g. `POSCAR`, `cml`, `xyz`). |
| `loadMolecule` | `content`, `format` | Read molecular data from a string in any format Avogadro can read, and make it the active molecule. |
| `getMolecule` | `format` (default `"cjson"`) | Return the active molecule as `{"format", "content"}`, in any format Avogadro can write. |
| `exportFile` | `fileName` | Write the active molecule, inferring the format from the extension. The write happens in the background: without `wait`, `true` means "started"; with `wait`, the reply comes when the file is on disk and reports its `fileName`. |
| `newMolecule` | none | Create a new empty molecule and make it active, like **File → New**. |
| `setActiveMolecule` | `index` | Make the open molecule at `index` (as `listMolecules` reports it) the active one. |
| `closeMolecule` | `index` (default: the active one), `discard` | Close a molecule. A molecule with unsaved changes is only closed if `discard` is `true`. Closing the last molecule leaves a new empty one. |

`newMolecule`, `setActiveMolecule` and `closeMolecule` report the active
molecule's `index` and the `count` of open molecules when sent with `wait`.

### Inspecting Avogadro

| Method | Parameters | Description |
|--------|-----------|-------------|
| `version` | none | `avogadroApp`, `avogadroLibs` and `qt` versions, `platform` (`macos`, `windows`, `linux` or `bsd`) and `rpcProtocol`, which is `2` for any version that supports `wait`. An older Avogadro answers `-32601`. |
| `listCommands` | none | Every method Avogadro will answer, sorted by name. Each entry has `name`, `description`, `kind` (`builtin`, `tool` or `extension`), the owning `plugin`, and `async`, which is `true` for anything that may finish after it replies. |
| `moleculeInfo` | none | Summary of the active molecule: `atomCount`, `bondCount`, `formula`, `mass`, `totalCharge`, `spinMultiplicity`, `coordinateSetCount`, `selectedAtomCount`, `residueCount`, `hasResidues`, `hasUnitCell`, `hasCustomElements`, `hasBasisSet`, `orbitalCount`, `homoIndex` (zero-based, `-1` without orbitals), `cubeCount`, `vibrationCount`, `fileName`, and the document state `modified`, `canUndo` and `canRedo`. |
| `listMolecules` | none | The open molecules, each with `index`, `active`, `atomCount`, `formula`, `fileName` and `modified`. |
| `listTools` | none | The tools of the active view, each with `name`, translated `displayName`, and `active`. |
| `listDisplayTypes` | none | The display types of the active view, each with `name`, translated `displayName`, `enabled`, `applicable` and `hasSettings`. |
| `activeDialog` | none | Whether a modal dialog is open: `open`, `title` and `className`. Answered even while another request is stuck behind that dialog. |
| `internalPing` | none | Answers `"pong"`. Handled by the RPC layer itself, so it works even before a window exists. |

### View and images

| Method | Parameters | Description |
|--------|-----------|-------------|
| `renderImage` | `width`, `height`, `transparentBackground`, `fileName` | Render the active view to a PNG. Give both `width` and `height` (each up to 8192), or neither for the view's own resolution. With `fileName`, the image is written there (`.png` is appended if there is no extension); without it, the PNG comes back base64-encoded in `data`. The reply also gives the `width` and `height` produced and the view's `nativeWidth` and `nativeHeight`. |
| `saveGraphic` | `fileName` | Save an image of the active view at its current on-screen size. `.png` is appended if the name has no extension. |
| `getCamera` | none | The camera's `distance` to its focal point, `focus` (x, y, z), `projection`, `orthographicScale`, and `modelView`: the 4×4 matrix as 16 numbers in row-major order. |
| `setCamera` | `modelView`, `projection`, `orthographicScale` | Apply any of these, as returned by `getCamera`; anything left out is unchanged. Answers with the resulting camera. |
| `setProjection` | `type`, or `perspective` / `orthographic` | Switch the camera projection. Either `{"type": "perspective"}` or a bare `{"orthographic": true}` key works. |
| `setRenderTypes` | `types`, or one key per type | Choose which display types are active — see below. |

`renderImage` renders at the size of the view and scales the result. When
the requested shape differs from the view's, the image is centered on a padded
canvas rather than reframed. See [Rendering images](develop-automation) for
practical advice.

### Undo, tools and layers

| Method | Parameters | Description |
|--------|-----------|-------------|
| `undo` / `redo` | none | Undo or redo the active molecule's last edit. Fails if there is nothing to undo or redo. With `wait`, reports `canUndo`, `canRedo`, `undoText`, `redoText` and `modified`. |
| `activateTool` | `name` | Make a tool active, by the `name` that `listTools` reports (e.g. `"Editor"`, `"Navigator"`). |
| `addLayer` | none | Add a layer to the active molecule, after the existing ones. Reports the new `layer` and the `count`. |
| `removeLayer` | `layer` | Remove a layer. The last remaining layer cannot be removed. |
| `setActiveLayer` | `layer` | Make a layer the active one; new atoms go into it. |
| `setLayerVisible` / `getLayerVisible` | `layer`, `visible` | Show or hide a layer, or report whether it is `visible`. |
| `setLayerLocked` / `getLayerLocked` | `layer`, `locked` | Lock or unlock a layer against edits, or report whether it is `locked`. |

The layer and tool methods behave like plugin commands: their results,
including the answer of `getLayerVisible` and `getLayerLocked`, only come back
when they are sent with `wait`. `visible` and `locked` must be JSON booleans.

### Display types

`setRenderTypes` takes either a list of names to turn on, leaving the others
as they are:

```json
{ "method": "setRenderTypes", "params": { "types": ["BallStick", "VanDerWaals"] } }
```

or a set of names mapped to booleans, which also lets you turn types off:

```json
{ "method": "setRenderTypes",
  "params": { "BallStick": true, "Wireframe": false } }
```

A name matches either a plugin's identifier or its translated display name.
Prefer the identifier — it does not change with the interface language.
`listDisplayTypes` lists them; in a standard build they are:

`BallStick`, `Cartoons`, `CloseContacts`, `CrystalScene`, `Dipole`, `Force`,
`Label`, `Licorice`, `NonCovalent`, `OverlayAxes`, `QTAIMScenePlugin`,
`SurfaceRender`, `SymmetryScene`, `VanDerWaals`, `Wireframe`

### Quitting

`kill` asks Avogadro to quit, but it is refused unless Avogadro was started
with `--testing`, which current versions do not accept on the command line.
End the process instead, as described in [Automation and Headless
Usage](develop-automation).

## Plugin commands

Tools and extensions register their own commands at startup, and any of them
can be sent as a JSON-RPC method name. `listCommands` shows which ones the
running Avogadro has. A few things hold for all of them:

* A command needs an open molecule, and fails with `No molecule` if there is
  none. `fetchByName` and `fetchPDB` are the exception, since they create one.
* Commands that belong to a tool (the Editor, Measure, Align, Navigator and
  Player tools) temporarily make that tool active, run, and then restore the
  tool you were using.
* Edits go through Avogadro's undo stack, so `undo` reverses them, unless
  noted otherwise. Freezing atoms and changing constraints are not undoable.
* Results are listed under **Returns**; remember they only arrive with
  `wait`.

### Databases

These replace the active molecule, so they do not need one to begin with.

| Command | Parameters | Description |
|---------|-----------|-------------|
| `fetchByName` | `name` | Download a structure by common or IUPAC name and load it. Queries the NIH Cactus resolver, then retries against PubChem's 3D endpoint if Cactus errors or returns 2D-only coordinates. |
| `fetchPDB` | `code` | Download a Protein Data Bank entry from RCSB and load it. `code` is the four-character identifier, the first character a digit 1-9 and the rest letters or digits. |

Both hand the work to the network, so send them with `wait`, which is what
the `fetch_by_name()` and `fetch_pdb()` helpers do for you. On success they
report the `name` that was fetched and the `source` that answered (`"cactus"`,
`"pubchem"` or `"rcsb"`), along with `atomCount` and `formula`; `fetchPDB`
adds `residueCount`. A code that is malformed, a name with no match, and a
download that cannot be read are all errors rather than empty successes.

```python
with connect() as avo:
    entry = avo.fetch_pdb("1crn")
    print(entry["formula"], entry["residueCount"])
```

### Selection

Every selection command returns the full list of selected atoms afterwards as
`indices`. Atoms in a locked layer are never selected.

| Command | Parameters | Description |
|---------|-----------|-------------|
| `selectAtoms` | `indices`, `mode` | Select atoms by index. `mode` is `"replace"` (the default), `"add"` or `"remove"`. Nothing changes if any index is invalid. |
| `selectAll` | none | Select every atom. |
| `selectNone` | none | Clear the selection. |
| `invertSelection` | none | Select the unselected atoms and deselect the rest. |
| `selectElement` | `element` | Select every atom of one element, given as a symbol (`"N"`) or atomic number (`7`), and deselect the others. |
| `selectWater` | none | Select water molecules: oxygens bonded to exactly two hydrogens, and residues named `HOH`. |
| `selectBackbone` | none | Select residue atoms named `CA`, `C`, `N` or `O` and the hydrogens on them. |
| `selectSidechains` | none | Select the other residue atoms. |
| `enlargeSelection` | none | Grow the selection to every atom within 2.5 Å beyond the selected atom farthest from the selection's center. |
| `shrinkSelection` | none | Shrink that sphere by 2.5 Å. |
| `createLayerFromSelection` | none | Move the selected atoms into a new layer, added after the existing ones. |

```python
with connect() as avo:
    avo.fetch_pdb("1crn")
    reply = avo.command("selectElement", element="S", wait=True)
    print(result_data(reply)["indices"])  # the six sulfur atoms
```

### Building and editing

The Editor commands respect locked layers: they fail if the active layer, or
any atom they would touch, is locked. They do not adjust hydrogens, so send
`adjustHydrogens` afterwards if you want that.

| Command | Parameters | Description |
|---------|-----------|-------------|
| `addAtom` | `element`, `position`, `bondTo`, `bondOrder` | Add an atom at `position` (`[x, y, z]` in Å). `element` is a symbol or atomic number. With `bondTo`, it is bonded to that atom with `bondOrder` 1–3 (default 1). Returns the new atom's `index`. |
| `addBond` | `atoms`, `order` | Bond two unbonded atoms, `[i, j]`, with `order` 1–3 (default 1). Returns the bond's `index`. Fails if they are already bonded. |
| `removeBond` | `atoms` | Remove the bond between two atoms. |
| `removeSelectedAtoms` | none | Delete the selected atoms and their bonds. Returns the number `removed`. Later atoms are renumbered. |
| `addHydrogens` | none | Add hydrogens to atoms with incomplete valences. |
| `removeHydrogens` | none | Remove hydrogens from atoms with too many. |
| `adjustHydrogens` | none | Both of the above. |
| `removeAllHydrogens` | none | Remove every hydrogen atom. |
| `createBonds` | none | Perceive bonds from interatomic distances, between all atoms or between selected atoms. Uses the tolerance set in **Configure Bonding**. |
| `removeBonds` | none | Remove all bonds, or every bond to a selected atom. |
| `addBondOrders` | none | Perceive bond orders. |
| `addCentroid` | none | Add a dummy atom at the geometric center of the molecule, or of the selected atoms. |
| `addCenterOfMass` | none | Add a dummy atom at the center of mass. |
| `addPerpendicular` | none | Add a dummy atom 2 Å from the center, perpendicular to the best-fit plane. |

The hydrogen, bonding and centroid commands act on the whole molecule (or the
selection, where stated) and return no data. Read the result back with
`moleculeInfo` or `getMolecule`.

### Measuring and constraints

The measure commands take `atoms`, a list of 2, 3 or 4 different atom
indices, and return them with the measured value. Distances are in Å, angles
and dihedrals in degrees, and the angle is the one at the middle atom.

| Command | Parameters | Returns |
|---------|-----------|---------|
| `measureDistance` | `atoms` | `distance` |
| `measureAngle` | `atoms` | `angle` |
| `measureDihedral` | `atoms` | `dihedral`, from -180 to 180 |
| `editDistance` | `atoms`, `value` (0.5–1000 Å) | the new `distance` |
| `editAngle` | `atoms`, `value` (0–180°) | the new `angle` |
| `editDihedral` | `atoms`, `value` | the new `dihedral` |

The edit commands keep the first atom fixed and move the fragment on the far
side of the relevant bond, or a whole separate molecule. If the atoms are
joined some other way, for example through a ring, the command fails with an
explanation rather than distorting the structure. The value returned is
measured after the move.

Constraints are applied by the next force field optimization. Their type
follows from the number of atoms: 2 for a distance, 3 for an angle, 4 for a
torsion.

| Command | Parameters | Description |
|---------|-----------|-------------|
| `listConstraints` | none | Returns `constraints`, a list of `{type, atoms, value}`. |
| `addConstraint` | `atoms`, `value` | Add a constraint, or update an existing one on the same atoms (in either order). Without `value`, the current geometry is used. Returns `type`, `atoms`, `value` and `updated`. |
| `removeConstraint` | `atoms` | Remove the constraint on these atoms, in either order. Returns the number `removed`; fails if none matched. |
| `clearConstraints` | none | Remove every constraint. Returns the number `removed`. |

### Force fields

| Command | Parameters | Description |
|---------|-----------|-------------|
| `listForceFields` | none | The force fields that suit the active molecule: `names`, `methods` (each `{id, name}`), `count`, `recommended`, and the `current` one. |
| `energy` | `method` | Calculate the energy. Returns `energy`, `unit` (`"kJ/mol"`) and the `method` used. |
| `forces` | `method` | Calculate the forces (the negative gradient), and show them as force arrows. Returns `forces`, one `[fx, fy, fz]` per atom in kJ/(mol·Å), plus `energy`, `rmsForce`, `maxForce`, `unit` and `method`. |
| `optimize` | `method`, `steps`, `gradientTolerance`, `energyTolerance` | Optimize the geometry, as one undo step. Returns `energy`, `unit`, `method`, the `steps` taken, `converged`, and the `reason` it stopped: `gradient`, `energy`, `maxSteps`, `optimizerStopped` or `nonFinite`. |
| `freezeSelected` | none | Freeze the selected atoms during optimization. Returns the `count`. |
| `unfreezeSelected` | none | Unfreeze the selected atoms. |
| `freezeAxis` | `axis` | Freeze one Cartesian axis of the selected atoms: `"x"`, `"y"`, `"z"` or `0`–`2`. |

`method` is an identifier from `listForceFields`, such as `"UFF"` or
`"MMFF94"`, and is case-sensitive. Without it, the force field chosen in
**Extensions → Calculate → Configure…** is used, and so are the saved defaults for
`steps` (250), `gradientTolerance` and `energyTolerance` (both 10⁻⁴).

`energy`, `forces` and `optimize` run in the background: always send them
with `wait`, and a longer `timeout` for large optimizations. An optimization
that runs out of `steps` still finishes successfully, so check `converged`.

### Symmetry

| Command | Parameters | Description |
|---------|-----------|-------------|
| `detectSymmetry` | `tolerance` | Detect the point group. Returns `pointGroup`, e.g. `"C2v"` or `"D∞h"`. |
| `symmetrize` | `tolerance` | Detect the point group and move the atoms onto it exactly. Returns `pointGroup` and `symmetryError`. |

`tolerance` is `"tight"`, `"normal"`, `"loose"` or `"veryloose"`. Pass it
explicitly: otherwise the setting in the Symmetry window is used if that window
has been opened, and `"tight"` if not.

### Moving the molecule and the view

| Command | Parameters | Description |
|---------|-----------|-------------|
| `centerAtom` | `index` (or `id`) | Move the molecule so that this atom sits at the origin. |
| `alignAtom` | `index` (or `id`), `axis` | Rotate the molecule about the origin so this atom lies along an axis: `"x"`, `"y"`, `"z"` or `0`–`2`. Send `centerAtom` first to rotate about a chosen atom. |
| `rotateScene` | `x`, `y`, `z` | Rotate the camera about the screen axes, through the focal point. One unit is 0.005 radians (about 0.29°), the same as one pixel of mouse drag. |
| `zoomScene` | `delta` | Zoom. Positive values move toward the focal point; one unit is about 2% of the distance to it. |
| `translateScene` | `x`, `y` | Pan the camera by a distance given in screen pixels. |
| `alignView` | none | Look down the z axis, centered on the molecule and backed off far enough to frame it. |
| `focusSelection` | none | Center the view on the selected atoms and zoom to fit them. |
| `unfocus` | none | Reset the view to show the whole molecule. |

`centerAtom` and `alignAtom` change the coordinates and can be undone; the
others only move the camera. For exact, repeatable views use `getCamera` and
`setCamera`.

### Colors

| Command | Parameters | Description |
|---------|-----------|-------------|
| `colorAtomsCustom` | `color` | Color all atoms, or the selected ones. |
| `resetAtomColors` | none | Go back to element colors, for all or the selected atoms. |
| `colorResiduesCustom` | `color` | Color all residues, or those whose `CA` atom is selected. |
| `colorResiduesByAminoAcid` | none | Color residues by amino acid. |
| `colorResiduesShapely` | none | Color residues with the Shapely scheme. |
| `colorResiduesBySecondaryStructure` | none | Color residues by helix, sheet, and so on. |
| `resetResidueColors` | none | Color residues by chain. |

`color` is a color name such as `"steelblue"` or a hex code such as
`"#4682b4"`. A missing or unreadable color answers `-32601`.

### Crystals

| Command | Parameters | Description |
|---------|-----------|-------------|
| `wrapUnitCell` | none | Wrap all atoms back into the unit cell, then perceive bonds again. |
| `standardCrystalOrientation` | none | Rotate the unit cell into the standard orientation. |
| `fillUnitCell` | `hallNumber` or `spaceGroup` | Add the symmetry-equivalent atoms, including copies on the cell faces, edges and corners. |
| `fillTranslationalCell` | `hallNumber` or `spaceGroup` | Add the symmetry-equivalent atoms, keeping only one copy of each atom on the cell boundary. |

The fill commands use the molecule's own space group, which most crystal file
formats provide. Otherwise, give one of:

* `hallNumber` — a Hall setting number from 1 to 530. This is *not* the
  International Tables number from 1 to 230.
* `spaceGroup` — a symbol that names a single setting, such as `"P 21/c"` or
  `"F d -3 m :2"`. A bare number like `"225"` works when that group has only
  one setting.

They never open a dialog; anything ambiguous is an error.

### Surfaces and orbitals

| Command | Parameters | Description |
|---------|-----------|-------------|
| `renderVanDerWaals` (or `renderVDW`) | `resolution` | van der Waals surface. |
| `renderSolventAccessible` | `resolution` | Solvent-accessible surface, with a 1.4 Å probe. |
| `renderSolventExcluded` | `resolution` | Solvent-excluded surface, with a 1.4 Å probe. |
| `renderMO` (or `renderOrbital`) | `orbital`, `isovalue`, `resolution`, `spin` | Molecular orbital, for a file that includes a basis set. |
| `renderElectronDensity` | `isovalue`, `resolution`, `spin` | Total electron density. |
| `renderSpinDensity` | `isovalue`, `resolution` | Spin density. |
| `renderCube` | `index`, `isovalue` | Draw an isosurface of a cube already in the file, counting from `1` (the default). |

Options:

* `orbital` — either a number, counting from one so that `1` is the lowest
  orbital, or a string relative to the frontier orbitals: `"homo"`, `"lumo"`,
  `"homo-1"`, `"lumo+2"`, and so on.
* `isovalue` — the isosurface value, default `0.03`. The three molecular
  surfaces do not use it.
* `resolution` — the grid spacing in Å. If it is left out, Avogadro picks a
  value from the size of the molecule, between 0.05 and 0.5 Å.
* `spin` — set to `"beta"` for the beta orbital or density of an
  open-shell calculation; alpha is used otherwise.

Each command replaces any surface already shown and turns on the surface
display type. Calculation runs in the background, so send it with `wait`
before saving an image. With `wait` it returns the `cubeIndex` (counting from
one), the `isovalue`, and the `resolution` actually used.

```python
with connect() as avo:
    avo.open_file("/path/to/acetone.out")
    avo.command("renderMO", orbital="lumo", isovalue=0.02, wait=True)
    avo.render_image(width=1600, height=1200, filename="/path/to/lumo.png")
```

### Vibrations and trajectories

Vibrational modes and coordinate sets (frames) are numbered from zero.

| Command | Parameters | Description |
|---------|-----------|-------------|
| `setVibrationalMode` | `mode` | Select a mode and show its displacement arrows. |
| `setVibrationalAmplitude` | `amplitude` | Set the animation amplitude on the same 0–99 scale as the dialog slider, which starts at 20. |
| `startVibrationAnimation` | none | Animate the selected mode until stopped. |
| `stopVibrationAnimation` | none | Stop the animation and restore the geometry. |
| `generateDisplacedCoordinates` | `modes` (or `mode`), `scale`, `structures` | Append coordinate sets displaced along one or more modes. `modes` is a list of mode numbers, `scale` defaults to 1.0, and `structures` (default 1) is how many displaced geometries to generate, spread evenly from `-scale` to `+scale`. |
| `showVibrations` | none | Open the vibrational modes window. |
| `nextFrame` / `previousFrame` | none | Step to the next or previous coordinate set, wrapping around at the ends. |
| `setCoordinateSet` | `index` | Show a particular coordinate set. |
| `coordinateSetCount` | none | Report without changing anything. |

The vibration commands return no data, and a missing `mode`, `amplitude`, or a
`scale` of zero answers `-32601`. The `vibrationCount` from `moleculeInfo`
gives the number of modes. The frame commands all return the current `frame`
and the `count` of coordinate sets.

### Windows

These open windows rather than computing something. Avoid them in unattended
scripts.

| Command | Description |
|---------|-------------|
| `showSpectra` | Open the spectra window, for a molecule with vibrational or other spectra. |
| `showMolecularProperties` | Open the molecular properties window. This also looks up the molecule's name on PubChem. |
| `showPdfPlot` | Plot the pair distribution function of a crystal. Asks for its options in a modal dialog first. |
| `showXrdPlot` | Plot a theoretical X-ray diffraction pattern of a crystal. Asks for its options in a modal dialog first, unless the file already includes an XRD pattern. |

A modal dialog holds up the reply until someone closes it. `activeDialog`
from a second connection shows what is open.

### Python plugin commands

Menu commands added by Python plugins are not available over RPC in 2.1: they
do not appear in `listCommands`, and calling one by name answers `-32601`.
Force fields provided by Python plugins *are* available, through
`listForceFields`, `energy`, `forces` and `optimize`.

## Adding commands from a plugin

Any C++ `ExtensionPlugin` or `ToolPlugin` can add to this vocabulary. Register
the names in `registerCommands()` and act on them in `handleCommand()`:

```cpp
void MyExtension::registerCommands()
{
  emit registerCommand("renderMovie",
                       tr("Render a movie of the current view. Options: "
                          "\"fileName\" (required) and \"frames\"."));
}

bool MyExtension::handleCommand(const QString& command,
                                const QVariantMap& options)
{
  if (command != "renderMovie")
    return false; // becomes a "Method not found" error

  const QString fileName = options.value("fileName").toString();
  if (fileName.isEmpty()) {
    emit commandFailed(tr("renderMovie requires a \"fileName\" option."));
    return true;
  }

  emit commandStarted();          // the work continues after we return
  startRendering(fileName);       // ...and calls movieFinished() when done
  return true;
}

void MyExtension::movieFinished(int frameCount)
{
  QVariantMap result;
  result["frames"] = frameCount;
  emit commandFinished(tr("Movie finished"), result);
}
```

The application collects these at startup, so a command is available as soon
as the plugin loads, and the description shows up in `listCommands`. Describe
the options there; it is the only documentation a script or an AI assistant
sees.

* Return `false` only for a command name you do not handle.
* For a command of yours that cannot run, emit `commandFailed()` with a
  message and return `true`. The caller gets error `-2` and the message,
  rather than a misleading `Method not found`.
* Emit `commandFinished()` with any results. Only values with a JSON
  equivalent survive the trip, so convert Eigen vectors and `Core::Array`
  data to lists of numbers first.
* If the work continues after `handleCommand()` returns, emit
  `commandStarted()` before returning. Every path must then end in
  `commandFinished()` or `commandFailed()`, or a waiting caller only hears
  back when its `timeout` runs out.
* Never open a modal dialog from a command. Take options from the request,
  and fall back to saved settings.

## Writing the packets directly

If you would rather not depend on the Python package, the protocol is small
enough to implement anywhere. In Python:

```python
import json
import socket
import struct
import tempfile


def read_exactly(sock, size):
    data = b""
    while len(data) < size:
        chunk = sock.recv(size - len(data))
        if not chunk:
            raise ConnectionError("Avogadro closed the connection")
        data += chunk
    return data


sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect(tempfile.gettempdir() + "/avogadro")

request = json.dumps({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "openFile",
    "params": {"fileName": "rutile.POSCAR"},
}).encode("utf-8")
sock.sendall(struct.pack(">I", len(request)) + request)

size = struct.unpack(">I", read_exactly(sock, 4))[0]
print(json.loads(read_exactly(sock, size).decode("utf-8")))
```

On Windows, open `\\.\pipe\avogadro` as an unbuffered binary file instead of
creating a socket; the framing and the JSON are identical.
