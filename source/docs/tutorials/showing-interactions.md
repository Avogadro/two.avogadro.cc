(tutorials-showing-interactions)=

# Showing Hydrogen Bonds and Other Interactions

Avogadro can draw non-covalent interactions as dashed lines, both between molecules (*intermolecular*, e.g., in a dimer or a protein–ligand complex) and within one molecule (*intramolecular*, e.g., an internal hydrogen bond). Two display types do this:

Non-Covalent
: Hydrogen bonds, halogen bonds and chalcogen bonds, checked against both distance and direction.

Close Contacts
: Atoms that are unusually close (possible clashes), plus salt bridges and repulsive contacts between charged groups.

## Show Hydrogen Bonds

As an example, build a short piece of DNA, whose base pairs are held together by hydrogen bonds.

1. Choose `Build` ⇒ `Insert` ⇒ `DNA/RNA…` and insert a short sequence (e.g., `GATTACA`), choosing **Double** so both strands are built. See {ref}`building-molecules-dna`.
2. In the [Display Types pane](panes-display-types-pane), check **Non-Covalent**.

Hydrogen bonds appear as dashed light blue lines between the bases.

% TODO(screenshot): /_static/tutorial-interactions-dna.png -- DNA base pairs with Non-Covalent enabled, H-bonds as dashed blue lines

The same works for any structure: a water cluster, a protein from the PDB (`File` ⇒ `Import` ⇒ `Fetch from PDB…`), or a host–guest complex.

:::{tip}
Hydrogen bonds need hydrogen atoms. Structures from the PDB and many crystal structures don't include them, so add them first with `Build` ⇒ `Hydrogens` ⇒ `Add Hydrogens`.
:::

## What Counts as an Interaction

The **Non-Covalent** display type looks for three kinds of interaction, each drawn in its own color:

| Interaction | Donor | Acceptor | Default color |
| --- | --- | --- | --- |
| Hydrogen bond | H bonded to N, O or F | N, O, F or Cl | Light blue |
| Halogen bond | F, Cl, Br or I bonded to C, N, O, F, S, Cl, Br or I | N, O, F or Cl | Green |
| Chalcogen bond | O, S, Se or Te bonded to C | N, O, F, S, Cl, Se or Te | Orange |

A line is drawn when the two atoms aren't bonded to each other, they're close enough, and they point at each other: the donor's bond should point roughly along the line to the acceptor, and the line should point roughly along one of the acceptor's lone pairs (worked out from the acceptor's hybridization). This avoids drawing a line between every pair of nearby atoms.

## Adjust the Settings

Click the **…** button next to **Non-Covalent** in the Display Types pane to open its settings. There's a tab for each kind of interaction, with:

Angle tolerance
: How far (in degrees) the geometry can be from ideal and still count. The default is 40°. Lower it to show only the most linear, strongest interactions.

Maximum distance
: How much longer than the sum of the two atoms' van der Waals radii the contact can be. The default is 1.0 Å for hydrogen bonds and 2.0 Å for halogen and chalcogen bonds.

Line width
: The width of the dashed lines.

% TODO(review): the Non-Covalent distance cutoff is the vdW-radius sum plus this value (H···O up to about 3.7 Å by default) -- check that this is the intended criterion

## Show Close Contacts and Salt Bridges

Check **Close Contacts** in the Display Types pane. It draws three kinds of contact, with a tab for each in its settings (the **…** button):

| Contact | Drawn between | Default distance | Default color |
| --- | --- | --- | --- |
| Contact | Any two atoms that aren't bonded to each other or to a common atom | 2.0 Å | Grey |
| Salt Bridge | Oppositely charged atoms | 4.0 Å | Purple |
| Repulsive | Atoms with the same charge | 4.0 Å | Red |

Here the distance is the actual distance between the atoms. With the default 2.0 Å, **Contact** lines show atoms that are probably too close, which is useful for spotting clashes after docking or building a complex by hand.

Charged atoms are those with a formal charge. In proteins, the side chains of Lys, Arg and His are also treated as positive, and those of Asp and Glu as negative, so salt bridges show up in a protein straight from the PDB.

% TODO(screenshot): /_static/tutorial-interactions-saltbridge.png -- a protein region with Close Contacts showing a purple salt bridge

## Focus on Part of a Structure

In a large system, lines everywhere can be hard to read. Use [layers](panes-layers-pane) to show interactions only where you need them: select the region of interest (e.g., a ligand and its binding pocket), choose `Select` ⇒ `Create New Layer from Selection`, then enable **Non-Covalent** or **Close Contacts** for that layer only. See {ref}`tutorials-hiding-hydrogens` for more about working with layers.

To get the exact length of an interaction, use the [Measure Tool](tools-measure-tool) and click the two atoms.

## See Also

- {ref}`display-types` – All display types
- {ref}`panes-display-types-pane` – Turning display types on and off
- {ref}`panes-layers-pane` – Working with layers
