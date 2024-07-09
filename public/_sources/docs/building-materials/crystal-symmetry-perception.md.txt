# Perceiving Crystall Symmetry

Calculation results often specify all atoms and translation vectors, but not the space group. Here we see how to perceive the space group from a set of crystallographic coordinates.

## Open a Crystal File

![](../../_static/open-a-crystal-file.png)

Here we open an example VASP calculation by opening the POSCAR file.

![](../../_static/media_1340332954652.png)

This example is triclinic, looking for Li / H structures. Note that VASP files do not specify a space group, so it is reported as "Unknown."

![](../../_static/media_1340332967365.png)

We can either set the spacegroup manually, or here, perceive the space group, using the open source spglib code.

![](../../_static/media_1340332976902.png)

We need to set the tolerance, since some atoms may be slightly out of place in Cartesian coordinates.

![](../../_static/media_1340332995909.png)

Our example VASP file isn't very interesting -- the space group is P1.

![](../../_static/media_1340333044109.png)

Here's another example, where the space group is P 1 21 1.

