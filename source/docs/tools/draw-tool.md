(tools-draw-tool)=

# Draw Tool

![The icon of the Draw Tool in light mode.](../../_static/icon_draw.svg)

Keyboard shortcut: <kbd>Ctrl</kbd>+<kbd>2</kbd>

Molecules are built and edited with the Draw Tool, which allows "free-hand" sketching of new molecules.

```{tip} **New in 2.0**
The default bond order setting is "Automatic" -- it will adjust intelligently with the length of the bond.
```

```{tip} **New in 2.0**
To help rapidly build your structure you can also use the new [Template Tool](tools-template-tool), which makes it quicker and easier to attach functional groups or assemble inorganic/organometallic complexes.
```

## Basic usage

Atoms and bonds are drawn using the mouse.

Left-clicking on an empty space in the view pane creates an atom of the currently selected element.

A left-click on an existing atom will change its element to the one currently selected.

Left-click and drag from an atom will create a new bond starting from that atom.
A new atom of the currently selected element is automatically created at the end of the new bond and is visible while dragging.

```{tip}
New atoms and bonds will be created in a plane that is parallel to the screen and includes the atom the bond originates from.
```

If, during the drag, the mouse is moved over an existing atom, the mouse will "snap" to it, and the new atom will disappear.
The new bond will be drawn to this existing atom instead.

By default, the bond order of a new bond is selected automatically based on the distance between the atoms: long bonds will be single bonds, short bonds will be double bonds, and very short bonds will be triple bonds.

A left-click on an existing bond will increase its bond order by one.
Left-clicking on a triple bond turns it back into a single bond.

Atoms and bonds can be deleted by right-clicking on them.

## Pane options

The currently selected element can be changed by selecting from the `Element` drop-down menu in the Draw Pane.

Various common elements are shown for easy access, but any element can be selected from the periodic table by choosing "Other…".
Used elements are remembered and will appear in the drop-down in future.

Alternatively, use the handy keyboard shortcuts -- just type the atomic symbol of the desired element (e.g., <kbd>O</kbd> for Oxygen, <kbd>A</kbd><kbd>s</kbd> for Arsenic).

The bond order of new bonds can be chosen with the `Bond Order` drop-down menu.
There are keyboard shortcuts for this too -- <kbd>1</kbd> selects single, <kbd>2</kbd> double, and so on.

When the bond order setting is set to "Automatic", new bonds are given a bond order based on their length.
The cut-offs are determined by the elements of the atoms at either end of the bond.

```{tip}
Single bonds are created when the bond length exceeds the sum of the atoms' covalent radii.
Double bonds are created when the bond length is between 91% and 100% of the sum of the covalent radii, and anything shorter than 91% becomes a triple bond.

For a carbon-carbon bond, the lower cut-offs are thus approx. 1.52 Å for a single bond and 1.38 Å for a double.
```

If the `Adjust Hydrogens` box is checked (default), extra hydrogen atoms will be automatically added to new atoms to satisfy their valency.
When a bond is created or the order of a bond is changed, the number of hydrogen atoms on the atoms at each end of the bond will be adjusted.

For main-group elements, the default valency is always that predicted by the octet rule, while metal atoms are always created alone, without bonded atoms.
To create metal centers or hypervalent main-group centers, it is often better to use the [Template Tool](tools-template-tool).

```{warning}
It may not be possible to deliberately add or remove hydrogen atoms (for example, to create a radical or an ion) while this setting is checked.

If this is desired, turn off the setting while manually adjusting the hydrogens.
Turning the setting back on will not cause the number of hydrogen atoms to be readjusted.
```

## Adjusting the structure

It is challenging to draw structures in 3D on a 2D screen.
Using the Draw Tool alone will probably not give you a molecule that looks sensible and is representative of the real geometry.

For manual adjustment, the position of the atoms can be fine-tuned by using the [Manipulation Tool](tools-manipulation-tool) in combination with the [Navigation Tool](tools-navigation-tool) to rotate and pan the view.

To quickly get a sensible geometry, make use of the [`Optimize Geometry`](calculations-optimization) extension.
This can be conveniently activated using the shortcut <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>O</kbd>.

## Tutorial

A step-by-step tutorial for some simple molecules can be found [here](tutorials-drawing-simple-molecules).