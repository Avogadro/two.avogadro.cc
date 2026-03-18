(menus-select-menu)=

# Select Menu

The Select menu contains commands that are useful for selecting atoms by various properties.

Select All {kbd}`Ctrl+A`
: Select all atoms

Select None {kbd}`Ctrl+Shift+A`
: Deselect all atoms

Invert Selection
: Select all atoms which are not currently selected, and deselect all currently selected atoms.

Select by Element
: Select all atoms of a certain element type.

Select by Atom Index
: Select atoms by a comma-separated list of indices. (does not deselect currently selected atoms)

:::{note}
This selection is 0-indexed, meaning the first atom in the XYZ has index 0.
:::

Select by Residue
: Select atoms in amino acids by their 3-letter identifiers

:::{note}
Residues must be specified in all caps.
:::

Select Backbone Atoms
: Select all atoms that belong to amino acid backbones

Select Sidechain Atoms
: Select all atoms that belong to amino acid sidechains

Select Water
: Select all water molecules

Enlarge Selection
: Select all atoms within 2 atoms of a selected atom. In other words, select all atoms next to a selected atom, and additionally all atoms that are next to those atoms.

Shrink Selection
: Shrink selection.

:::{warning}
One shrink is equivalent to **two** enlarges!
:::

Create New Layer from Selection
: Separate the selected atoms into a new layer.
