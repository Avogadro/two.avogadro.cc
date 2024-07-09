(tools-manipulation-tool)=

# Manipulation Tool

The Manipulation Tool allows you to move individual atoms as well as fragments.

![](../../_static/520ebec1-6470-4f93-af26-c94ac5ea6f9d.png)

If one or more atoms have been selected with the [Selection Tool](tools-selection-tool), all operations will be carried out on the entire selection as one unit. If nothing has been selected, whichever atom is dragged will be moved.

## Basic usage

Atoms can be translated by clicking and dragging with the left mouse button.

```{tip}
When translating with click and drag, atoms will always move parallel to the screen; their depth will not change. For effective positioning within 3D space, it is thus necessary to combine the Manipulation Tool with the Navigation Tool to rotate the molecule.
```

Atoms can be rotated by clicking and dragging with the right mouse button.

```{tip}
Rotation with click and drag will always be about the geometric center of the selection.
```

The Manipulation Tool is automatically selected after inserting a fragment, to enable quick and easy positioning of the new fragment.

## Pane options

The options in the Manipulate Pane allow you to apply transformations mathematically to the currently selected atoms.

Shifts along the X-, Y-, and Z-axes can be specified in angstrom.

![](../../_static/0f89679e-9bee-4005-8793-fc96682ecd34.png)

The "Rotate around:" section allows you to rotate your selection around the current geometry, or the origin. After choosing how many degrees to rotate your selection click "Apply".

![](../../_static/14c1bee4-7288-4fa7-8660-d9fc58578631.png)

Clicking "Reset" will reset all information in the translation, and rotation boxes. This does not reset the molecule, if you want to undo your adjustments go to the "Edit" menu in the top bar and select "Undo Manipulate Atom".

![](../../_static/e711ffa1-6a52-4748-af42-e734581bf36b.png)

The icon for the Manipulation Tool is adapted from a design by [Ryan Dell](https://thenounproject.com/ryandeel/), a contributor to the Noun Project.