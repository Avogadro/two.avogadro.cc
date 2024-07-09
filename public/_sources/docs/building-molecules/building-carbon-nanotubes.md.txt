# Building Carbon Nanotubes

Avogadro 1.1 includes a new nanotube builder, based on the well-known TubeGen code and website from the Doren group at U. Delaware. \([http://turin.nss.udel.edu/research/tubegenonline.html](http://turin.nss.udel.edu/research/tubegenonline.html)\)

![](../../_static/media_1340334543445.png)

Under the Build menu, there’s a new option for the nanotube builder. At the moment only single-walled nanotubes \(SWNT\) can be built in one step, although it’s easy to generate several nested tubes for multi-walled \(MWNT\) as shown here.

![](../../_static/media_1340334581991.png)

The builder will show up at the bottom of the Avogadro window. You can set the n,m indexes to determine the type of nanotube \(1\) the length of the tube \(2\), in Angstrom, bohr, picometers, nanometers, or periodic unit cells \(e.g., if you wish to do a calculation with periodic boundar conditions\), and how to terminate the nanotube \(3\). **NOTE**: determining double bonds can be time-consuming on large nanotubes.

![](../../_static/media_1340334958508.png)

The nanotube will be generated aligned along the z-axis, so you may want to re-center the view.

![](../../_static/media_1340335027391.png)

Here, we've added a 6,6 nanotube after inserting our 4,4 nanotube. We'll need to re-center the tube to produce a more accurate double-walled system.

![](../../_static/media_1340335238130.png)

Here, we use the manual translation options, new in Avogadro 1.1, to “nudge” the 6,6 nanotube in the XY plane to properly center around the 4,4 nanotube.

![](../../_static/media_1340335304968.png)

Here we’ve nudged the 6,6 tube into an approximately correct position. We’ll now use Avogadro’s built-in force fields and the Auto-Optimize tool to relax the structure.

![](../../_static/media_1340335406817.png)

We \(1\) select the Auto-Optimize tool to allow interactive minimization of the nanotubes, and \(2\) select the MMFF94 force field. Other forcefields would also likely work well. Finally \(3\) start the optimization.

![](../../_static/media_1340335353244.png)

After a few steps, you can see a nicely relaxed double-walled nanotube. You could repeat the process as desired.

