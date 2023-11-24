# Interface Changes

Many parts of the interface have changed in Avogadro 2.

```{warning}
When saving files, File => Save allows saving to CJSON and CML formats,
which will retain all data and options.

If you wish to **export** to other formats (e.g., XYZ, PDB, SDF, etc.) use
File => Export => Molecule…
```

![Screenshot indicating File => Export => Molecule menu item](../../_static/FileExportMolecule.png)

During the development of Avogadro 2 betas, the interface is currently in flux,
and menu items and tool icons will change.

Consequently, this documentation is still a work in progress. Some instructions and screenshots may be out of date.

## Input Generators

The *input generators* which help format input for external programs like Gaussian, ORCA, CP2K, and LAMMPS have moved into a new "Input" menu of their own.

Many of these menu items use [Python scripts](input-generators), so if your menu does not include many options, make sure that Python is installed and configured.

![Screenshot indicating Input menu and commands from Python scripts](../../_static/InputMenu.png)
