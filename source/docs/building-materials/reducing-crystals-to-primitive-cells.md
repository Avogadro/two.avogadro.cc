# Reducing Crystals to a Primitive Unit Cell

Some simulations use "supercells" -- larger periodic boundary systems than the primitive unit cell. Here is a walk-through on reducing a large supercell to the primitive unit cell.

![](../../_images/media_1340336029160.png)

Open or import the file with the supercell -- here, CaCO3. Note that the space group is unknown, since the file came from VASP, which does not specify a space group with the coordinates.

![](../../_images/media_1340336076337.png)

After perceiving the space group, we see correctly that the system is R -3 c. Now we can reduce the supercell to a primitive cell of CaCO3.

![](../../_images/media_1340336318568.png)

Avogadro provides two algorithms for reducing the unit cell to a primitive or Niggli cell. Here, pick "Primitive." Note that the volume of this supercell was over 4,000 Å3.

![](../../_images/media_1340336361329.png)

You will need to set a tolerance for the Cartesian coordinates \(here, in Å\).

![](../../_images/media_1340336453963.png)

After reduction, note that the space group is retained, the lattice is properly Rhombohedral, and the unit cell volume is 36 times smaller.

