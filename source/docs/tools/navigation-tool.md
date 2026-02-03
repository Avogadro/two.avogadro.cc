(tools-navigation-tool)=

# Navigation Tool

![The icon of the Navigation Tool in light mode.](../../_static/icon_navigate.svg)

Keyboard shortcut: <kbd>Ctrl</kbd>+<kbd>1</kbd>

The **Navigation Tool** is used to **rotate**, **pan**, and **zoom** the view of a molecule within the view pane.

Only the perspective of the view is changed, and the positions in space of all atoms are preserved.
To move atoms, fragments, or molecules within 3D space, use the [Manipulation Tool](tools-manipulation-tool) instead.

:::{tip}
When using any of the other tools, if a mouse or keyboard action is not defined for that tool but it is defined for the Navigation Tool, the action will have the same effect as if the Navigation Tool was selected.

This means that many of the below actions will also work from some other tools.
For example, left-click and drag will also rotate the view while the [Animation Tool](tools-animation-tool) is selected.
:::

## Basic Usage

### With the Mouse

**Rotate** the view by clicking and dragging anywhere on the view pane with the **left mouse button**.

This rotates the view around the x- and y-axes (from your perspective, not the coordinate axes).

To rotate the view around the z-axis (the axis you are looking down), hold the **middle mouse button** and drag, or hold <kbd>Shift</kbd> while clicking and dragging with the left mouse button.

Moving the mouse in a particular direction will rotate the view such that the part of the molecule nearest to you moves in the same direction.
For example, clicking and dragging to the left will cause the molecule to rotate clockwise (as considered looking from the top down).

:::{tip}
Rotation with click and drag will always be about the geometric center of the molecule.
:::

**Pan** the view in the xy-plane (parallel to the screen) by clicking and dragging with the **right mouse button**, or by holding <kbd>Ctrl</kbd> while clicking and dragging with the left mouse button.

Again, when panning, the molecule will move in the direction the mouse is moved in.

Panning along the z-axis, i.e. changing the **zoom level** can be done using the **mouse scroll wheel** or by clicking and dragging with the **middle mouse button**.

### With the Keyboard

All the above view transformations can also be done using only the keyboard.
This can be done using any of three different sets of directional keys: the arrow keys, WASD, or HJKL.
They are equivalent as follows:

- <kbd>↑</kbd> = <kbd>W</kbd> = <kbd>K</kbd> (here collectively referred to as <kbd>up</kbd>)
- <kbd>↓</kbd> = <kbd>S</kbd> = <kbd>J</kbd> (<kbd>down</kbd>)
- <kbd>←</kbd> = <kbd>A</kbd> = <kbd>H</kbd> (<kbd>left</kbd>)
- <kbd>→</kbd> = <kbd>D</kbd> = <kbd>L</kbd> (<kbd>right</kbd>)

**Rotate** the view around the **x- and y-axes** using the directional keys **without modifiers**.

**Rotate** the view around the **z-axis** by holding <kbd>Shift</kbd> while using <kbd>left</kbd> and <kbd>right</kbd>.

**Pan** the view along the **x- and y-axes** by holding <kbd>Ctrl</kbd> while using the directional keys.

:::{warning}
Currently, panning with <kbd>Ctrl</kbd>+<kbd>W</kbd>/<kbd>A</kbd>/<kbd>S</kbd> will not work because those shortcuts are mapped to other functionality.
In future, keyboard control of the Navigation Tool will not use <kbd>Ctrl</kbd> at all.
:::

**Pan** the view along the **z-axis**, i.e. **zoom**, by holding <kbd>Shift</kbd> while using <kbd>up</kbd> and <kbd>down</kbd>.

## Options

Reverse Direction of Zoom on Scroll
: Toggle the direction that is zoomed when scrolled.

  Note that the default behavior is determined by your operating system's settings.

:::{note}
The icon for the Navigation Tool is a design by [Dekin Dorcas](https://thenounproject.com/creator/ddorcas/), a contributor to the Noun Project.
:::

## See Also

- {ref}`tools-manipulation-tool` – Move atoms in 3D space (not just the view)
