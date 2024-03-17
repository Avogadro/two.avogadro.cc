(tools-navigation-tool)=

# Navigation Tool

![The icon of the Navigation Tool in light mode.](../../_static/icon_navigate.svg)

Keyboard shortcut: <kbd>Ctrl</kbd>+<kbd>1</kbd>

The Navigation Tool is used to rotate, pan, and zoom the view of a molecule within the view frame.

Only the perspective of the view is changed, and the positions in space of all atoms are preserved.
To move atoms, fragments, or molecules within 3D space, use the [Manipulation Tool](tools-manipulation-tool) instead.

```{tip}
When using any of the other tools, if a mouse or keyboard action is not defined for that tool but it is defined for the Navigation Tool, the action will have the same effect as if the Navigation Tool was selected.

This means that many of the below actions will also work from some other tools.
For example, left-click and drag will also rotate the view while the [Animation Tool](tools-animation-tool) is selected.
```

## Basic usage

The view can be rotated by clicking and dragging anywhere on the view frame with the left mouse button.

Moving the mouse in a particular direction will rotate the view such that the part of the molecule nearest to you moves in the same direction.
For example, clicking and dragging to the left will cause the molecule to rotate clockwise (as considered looking from the top down).

```{tip}
Rotation with click and drag will always be about the geometric center of the molecule.
```

The view can be panned by clicking and dragging with the right mouse button.

Again, when panning, the molecule will move in the direction the mouse is moved in.

The zoom level can be increased and decreased using the mouse scroll wheel.

## Pane options


