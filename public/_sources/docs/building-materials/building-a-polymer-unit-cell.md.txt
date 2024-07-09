# Building a Polymer Unit Cell

A walk-through on creating a unit cell \(of a polymer\) using Avogadro and the Align tool. This specific example uses Gaussian, but translation vectors for other programs can be performed similarly.

![](../../_static/media_1260118979959.png)

Build out the molecule for the unit cell. Notice that while the repeat unit here is 2 rings, we have built 3 rings. This way, we will properly model the bond which spans two unit cells.

![](../../_static/media_1260119377141.png)

Optimize the geometry of the molecule.

![](../../_static/media_1260119456591.png)

Switch to the Align tool to translate and orient the unit cell coordinates.

![](../../_static/media_1260119601872.png)

Make sure to open the Tool Settings window, which will allow you to work with the Align tool.

![](../../_static/media_1260119685502.png)

First click on the "start" atom of the polythiophene. This atom will be translated to the origin \(0, 0, 0\). Then click on the corresponding atom in the "next" unit cell. The distance between these two atoms will define one axis in the unit cell.

![](../../_static/media_1260119852731.png)

In the "Align Settings" window, define an axis for the unit cell. Then click the Align button. This will change the coordinate set to have atom \#1 at the origin, and atom \#2 \(from the step above\) projected onto the x-axis.

![](../../_static/media_1260120107101.png)

Open the Cartesian Editor window to verify the results of the Align operation.

![](../../_static/Screen-shot-2009-12-06-at-12.23.01-PM.png)

Notice that atom \#1 is at the origin, and atom \#11 is projected onto the X-axis. The size of the unit cell is 7.806Å -- the distance between atom \#1 and atom \#11.

![](../../_static/media_1260120454671.png)

Now delete "extra" atoms which should not be included in the unit cell calculations. This includes the third ring \(including atom 11\) and the "end" hydrogen atoms. For example, you can use the select tool and drag over the atoms to be deleted to pick them.

![](../../_static/media_1260120552391.png)

Once selected, you can use the "Clear" menu command to delete the atoms.

![](../../_static/media_1260120773167.png)

If you wish to submit the unit cell to Gaussian, pick the Gaussian input extension.

![](../../_static/Screen-shot-2009-12-06-at-12.36.05-PM.png)

Set options as you desire. Make sure to add a "TV 7.806 0.0 0.0" line at the bottom of the preview text. This will enable the unit cell calculation by setting the translation vector for the unit cell.

