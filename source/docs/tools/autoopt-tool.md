(tools-autoopt-tool)=

# AutoOptimization Tool

![The icon of the AutoOpt Tool in light mode.](../../_static/icon_autoopt.svg)

Keyboard shortcut: <kbd>Ctrl</kbd>+<kbd>7</kbd>

The **AutoOpt Tool** is used to optimize the geometry of a molecule interactively, including editing or moving atoms.

## Basic Usage

![][1]

[1]: ../images/7-auto-optimize-tool/27bc0d24-9f97-4a7c-9910-437a3543a1a1.png

Select a method to optimize the system. Depending on the elements in your
molecule, the total charge on the system, etc. different methods may be available. (For example, not all methods work with crystals and unit cells.) By default both the UFF and Lennard-Jones (LJ) models are available for all systems. Molecules will reoptimize until dE=0 or "Stop" is clicked.

The default force field in Avogadro is UFF (Universal Force Field). UFF can generally reproduce the most structural features across the periodic table. Other methods may provide better geometries for organic molecules (e.g., GAFF or MMFF94) and you can install additional methods as plugins including a wide variety of machine learning (ML) potentials.

![][8]

[8]: ../images/7-auto-optimize-tool/ba606487-98a6-4d53-8319-e8a5ea3890b6.png

## See Also

- {ref}`optimize` – Overview of geometry optimization methods in Avogadro
- {ref}`optimize-force-fields` - Overview of different force field methods
- {ref}`optimize-constraints` – Freeze atoms, fix distances, angles, and dihedrals during optimization

