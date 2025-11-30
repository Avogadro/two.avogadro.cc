(menus-build-menu)=

# Build Menu

The Build menu contains commands useful for creating and modifying molecular geometries.

Atomic Coordinate Editor
: Open the [Atomic Coordinate Editor](coordinate-editor).

Insert
: See [Insert](insert-dropdown).

Hydrogens
: See [Hydrogens](hydrogens-dropdown).

Bond
: See [Bond](bond-dropdown).

Change Elements
: Change the selected atoms to a chosen element.

Add Centroid
: Add a dummy atom at the geometric center of the molecule.

Add Center of Mass
: Add a dummy atom at the center of mass of the molecule.

Add Perpendicular
: TODO

(coordinate-editor)=
#### Atomic Coordinate Editor

The Atomic Coordinate Editor is an extremely useful environment for modifying the existing molecular structure, formatting a set of coordinates, and reordering atomic indices.

The window has several useful features:

Preset
: Select a preset format for the coordinates and update any existing coordinates.

Format
: Specify a custom format for the coordinates (the Help menu on the right includes more information)

Distance Unit
: Select between Angstroms (Å) and Bohrs/Atomic Units (a.u.).

:::{note}
1 Å    = 1.88972613 Bohrs

1 Bohr = 0.52917721 Å
:::

Revert
: Reverts any edits.

Clear
: Clears all coordinates.

Apply
: Applies any edits.

:::{note}
The text in the coordinate box will appear green when it has been edited, and black after being applied.
:::

(insert-dropdown)=
#### Insert

Molecule
: Insert a **molecule fragment** from the [Molecules Plugin](extensions-plugins-menu).

DNA/RNA
: Insert **DNA/RNA** fragments using the [Nucleic Acid Builder](nucleic-acid-builder).

InChI
: Insert a molecule using an International Chemical Identifier ([InChI](https://www.inchi-trust.org/)).

SMILES
: Insert a molecule using a [SMILES](https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html) string.

(hydrogens-dropdown)=
#### Hydrogens

Adjust Hydrogens {kbd}`Ctrl+Alt+H`
: Add any missing hydrogen atoms, and remove any extra hydrogen atoms on any atoms that violate the octet rule.

Add Hydrogens
: Add any missing hydrogen atoms on atoms that have incomplete octets.

Remove Extra Hydrogens
: Remove any extra hydrogen atoms on atoms with overfull octets.

Remove All Hydrogens
: Remove all hydrogen atoms in the molecule.

(bond-dropdown)=
#### Bond

Bond Atoms {kbd}`Ctrl+B`
: Bond all atoms in the molecule.

:::{warning}
This will change all existing bonds to single bonds!
:::

Bond Selected Atoms
: Bond all selected atoms.

Perceive Bond Orders
: Check all atoms that have unsatisfied octets and add enough double or triple bonds to satisfy the octet.

Remove Bonds {kbd}`Ctrl+Shift+B`
: Remove bonds containing selected atom, or remove all bonds in document if there are no selected atoms.

Configure Bonding
: TODO