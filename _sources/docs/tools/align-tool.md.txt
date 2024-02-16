(tools-align-tool)=

# Align Tool

![The icon of the Align Tool in light mode.](../../_static/icon_align.svg)

The Align Tool is used to rotate and translate a molecule(s) so that it aligns with one of the Cartesian axes.

## Basic usage

First, an alignment axis is chosen from the `Axis` drop-down menu in the Align Pane. The <kbd>x</kbd>, <kbd>y</kbd>, and <kbd>z</kbd> keys on the keyboard are shortcuts for changing the alignment axis.

Secondly, select either one or two atoms in the view frame with the left mouse button. The labels #1 and #2 will be displayed on each.

Clicking `Align` will then reposition the molecule as desired.

If only one atom was selected, the molecule will simply be translated so that it is placed at the origin (i.e. the Cartesian coordinates (0,0,0)).

If two atoms were selected, the first will be placed at the origin, and the second will be placed along the chosen axis.

```{tip}
The red axis is designated as the X axis, green is designated as the Y axis, and blue is designated as the Z axis.
```

## Pane options

![](../../_static/e3143779-956e-4d83-ac28-dc2f79bf2194.png)

The `Axis` drop-down menu allows you to choose which Cartesian axis the molecule will be aligned to.

![](../../_static/ec6c967d-5df0-41b8-b692-93123f8a0462.png)

By default, the relative positions of everything in the view frame will remain the same and the same transformation will be applied to all objects. By choosing the "Molecule" option in the `Align` drop-down menu in the Align Pane, only the molecule containing the selected atoms will be affected by the change.

![](../../_static/c1839173-f147-444d-b9c9-9ebb2e0a28f4.png)

![](../../_static/ca04487a-6f68-45ca-a5bf-92a2daf99194.png)

