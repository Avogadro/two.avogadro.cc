(display-types)=

# Display Types

Avogadro offers several display types to customize your molecular display
and offer high-quality publication-ready graphics.

![Display Types panel, outlined in red, below the Draw tool settings. It lists Ball and Stick, Cartoons, Close Contacts and other display types, each with a checkbox and some with a ⋯ button](../../_static/locating-display-types.png)

Clicking on the ⋯ icon located on the right of some display types will allow various adjustments to be made to the display. For example, you can edit the opacity of the Van der Waals Spheres so that you can still view the ball and stick model underneath.

![Display Types panel with Van der Waals checked. Marker 1 points to its ⋯ button, and marker 2 to the Opacity slider that appears under View Configuration](../../_static/vdw-opacity.png)


## Ball and Stick

Ball and Stick is the default display style when Avogadro is opened. This provides the standard ball and stick representation of a molecule.

![Avogadro window showing caffeine in the default ball-and-stick style, with the Display Types panel on the left](../../_static/caffeine-window.png)

## Cartoons

The cartoon feature only applies to secondary biological structures (e.g. α helix and β sheet). Below is the cartoon for a protein.

![Protein drawn as light blue cartoon ribbons tracing its helices, with the atoms also shown as ball and stick](../../_static/cartoon.png)

## Close Contact

:::{versionadded} 2.0
The Close-Contact style indicates atoms near each other even if not directly bonded, including salt bridges and repulsive interactions in biomolecules.
:::

![Close Contacts style: dashed gray lines from a CH2 carbon to a nearby bromine atom (dark red) and chlorine atom (green)](../../_static/close-contact.png)


## Dipole Moment

The Dipole plugin will display an overall net dipole if one is present.

![Water molecule with a green dipole moment arrow drawn from the oxygen along the bisector of the H–O–H angle](../../_static/dipole.png)

## Force

The Force plugin displays green arrows on atoms (as shown below), to qualitatively demonstrate the forces being applied to the atoms.

![Caffeine in ball and stick with green arrows on the atoms, showing the direction and relative size of the force on each atom](../../_static/force.png)

## Label

The label plugin numbers and labels atoms, bonds, or residues in a molecule.

![Avogadro 1 window showing aspartame with each atom labeled by element and number, such as C1, O2, N1 and H13](../../_static/label.png)

## Licorice

Licorice or "sticks" minimizes spheres for the atoms, instead drawing the covalent bond skeleton of the molecule.

![Caffeine in the Licorice style: bonds drawn as thick rounded sticks colored by element, with no separate atom spheres](../../_static/stick.png)

## Non-Covalent

The Non-Covalent style demonstrates implicit non-covalent interactions between atoms.

:::{versionadded} 2.0
In Avogadro 2, in addition to display of hydrogen bonds, the Non-Covalent style can show Halogen and Chalcogen bonds (e.g., S-S non-covalent interactions).
:::

![Cytosine and guanine nucleotides paired by three hydrogen bonds, drawn as light blue dotted lines between the bases](../../_static/hydrogen-bond.png)


## QTAIM (Quantum Theory of Atoms in Molecules)

QTAIM displays the implicit bonding that is theorized to take place between the hydrogens of organic crystals (the implicit bonding is conveyed through dots). This display type is utilized by importing a .wfn file from the "QTAIM", "Molecular Graph" selection under the "Extensions" menu. More information can be found on this process in the {ref}`QTAIM Tutorial<qtaim>`.

![QTAIM molecular graph of two phenol molecules. Critical points appear as small magenta, blue and yellow spheres along the bond paths, and dotted lines trace bond paths between the two molecules](../../_static/phenol-qtaim.png)

## Reference Axes

Clicking on the Axes plugin will provide the Cartesian axes in the bottom left corner of the view. Note that the red, green, and blue arrows represent the x, y, and z axes respectively.

![Caffeine with the reference axes in the lower-left corner, circled in yellow: a red x arrow pointing right, a green y arrow pointing up, and the blue z axis pointing out of the screen](../../_static/reference-axes.png)


## Surfaces

Once a surface has been created (Extensions Menu -> Create Surfaces...), the Surface display type can be used. This display type allows adjustments to the orbital, opacity, rendering, style, and color.

![Benzene with a translucent π molecular orbital surface, its lobes of opposite sign shown in blue and yellow](../../_static/surfaces.png)


## Symmetry Elements

:::{versionadded} 2.0
The new symmetry perception feature includes rendering rotation axes, mirror planes, and other symmetry elements in molecules.
:::

![C180 fullerene cage in ball and stick with its symmetry elements: red rotation axes passing through a blue inversion center in the middle](../../_static/C180.png)


## Van der Waals Spheres

The Van der Waals plugin provides the classic sphere rendered Van der Waals image.

![DNA double helix drawn as space-filling Van der Waals spheres colored by element](../../_static/van-der-waals-spheres.png)

## Wireframe

Wireframe draws atoms and bond order into the molecule.

![DNA double helix in the Wireframe style: thin lines for bonds, colored by element, with no atom spheres](../../_static/wireframe.png)

```{toctree}
---
caption: Display Types
---
Introduction <self>
coloring-molecules
```
