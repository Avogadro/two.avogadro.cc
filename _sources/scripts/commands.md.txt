(command-scripts)=

# Command Scripts

Command scripts work similarly to generators - passing JSON to
Avogadro to render a form interface and then perform work. In principal,
the scripts can be written in any programming language, although most
are currently written in Python.

This guide will cover the UI aspects of scripts, with separate
discussion of generators and command operation elsewhere.

## Script Entry Points

The script *must* handle the following command-line arguments:

- `--debug` Enable extra debugging output. Used with other commands.
  It is not required that the script support extra debugging, but it
  should not crash when this option is passed.
- `--lang XX` Display the user interface with a specific language or
  localization. It is not required that scripts support localization,
  but it should not crash when this option is passed.
- `--print-options` Print the available UI options supported by the
  script, e.g. simulation parameters, etc. See below for more details.
- `--display-name` Print a user-friendly name for the script. This is
  used in the GUI for menu entries, window titles, etc.
- `--menu-path` Print the expected menu path for the script,
  separated by "|" characters (e.g., "Extensions|Quantum" or
  "Build|Insert"). The final part of the menu path will include the
  display-name.

## Specifying UI options with --print-options

The format of the `--print-options` output must be a JSON object of
the following form:

```
{
  "userOptions": {
    ...
  },
  "inputMoleculeFormat": "cjson"
}
```

The `userOptions` block contains a JSON object keyed with option names
(e.g. "First option name"), which are used in the GUI to label
simulation parameter settings. Various parameter types are supported.

If the command does not require an options dialog, the JSON can be completely empty. or include an empty `userOptions` block.

## Returning Data

Avogadro will pass JSON on the standard input, including the `userOptions` selections as well as the molecular data as requested.

After running the script, data should be printed to the standard output in JSON format, e.g.

```json
{
  "cjson": {}
}
```

### Returning Data in a Specific File Format

While the default is for data to be returned as `cjson` objects, scripts can return data in any format recognized by Avogadro. In general, we suggest `mol` or `sdf`, `xyz`, `pdb`, `cif`, `cml`, or `cjson` as relatively common interchange foramts.

To indicate the format use the `moleculeFormat` key and then return the file data with the appropriate key:

```json
{
  "moleculeFormat": "pdb",
  "pdb", "…" // PDB file as a string
}
```

### Appending New Atoms and Bonds

Sometimes a script may wish to `append` new atoms and bonds to the current system. As indicated above, the default action is to replace the current molecule with data returned to Avogadro (e.g., deleting or replacing atoms, etc.).

Instead, one can use the `append` key in the JSON returned to Avogadro:

```json
{
  "moleculeFormat": "pdb",
  "append": true
}
```

Avogadro will not modify the existing molecule, but only insert new atoms and/or bonds.

### Bonding New Atoms

Avogadro can perceive bonds and bond orders in the new or appended molecule. Simply supply the `bond` key in the JSON returned to Avogadro, for example:

```json
{
  // other data to return, e.g. in XYZ format
  "moleculeFormat": "xyz",
  "append": true,
  "bond": true
}
```

### Selected Atoms

A script can indicate atoms to select in the current molecule using the `selectedAtoms` key in the JSON returned to Avogadro. The `selectedAtoms` should be a numeric list, e.g.

```python
    # e.g., matching a SMARTS pattern
    for match in mol.GetSubstructMatches(smarts):
        for atom in match:
            selected.append(atom)
 
    # Just indicate that we want to select matching atoms
    result = {
        'selectedAtoms': selected
    }
```

## Debugging

Debugging may be enabled by defining `AVO_PYTHON_SCRIPT_DEBUG` in the process's
environment. This will cause the `--debug` option to be passed in
all calls to scripts, and will print extra information to the
qDebug() stream from within Avogadro (i.e., to the console). 
The script is free to handle the debug flag as the author wishes.


```{toctree}
---
caption: Command Scripts
hidden: true
---
commands
example1
example2
```
