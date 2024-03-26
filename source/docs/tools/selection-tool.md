(tools-selection-tool)=

# Selection Tool

![The icon of the Selection Tool in light mode.](../../_static/icon_select.svg)

Keyboard shortcut: <kbd>Ctrl</kbd>+<kbd>5</kbd>

The **Selection Tool** is used to **select atoms** with the mouse, either by individually picking them out or using a marquee selection box.

:::{tip}
Further useful selection functionality is available in the [`Select` menu](menus-select-menu).
:::

## Basic usage

**Left-click** on an individual atom to **select** it.

![A single atom selected after clicking on it.](../../_static/tutorial-select-atom.png){height=300px align=center}

**Left-click and drag** to **select multiple** atoms by drawing a marquee selection box that covers the desired selection.

![A selection box as visible while dragging.](../../_static/tutorial-select-drag.png){height=300px align=center}

Hold <kbd>Shift</kbd> or <kbd>Ctrl</kbd> while selecting atoms to **add them** to the current selection.
This works for both the above selection methods.

**Double-left-click** on an atom to instantly **select all connected atoms**.
"Connected" atoms are any that can be traced to the clicked atom through bonds, including over multiple bonds i.e. the whole molecule or fragment.

![An entire molecule selected after clicking on one of its constituent atoms.](../../_static/tutorial-select-all.png){height=300px align=center}

:::{tip}
Use `Select`⇒`Enlarge Selection` to increase the selection from an atom to only its immediate neighbors rather than the whole molecule.
:::

Hold <kbd>Ctrl</kbd> and **double-left-click** on an atom to select the **inverse** of the current selection; the currently selected atoms will be deselected, and all other atoms of the molecule will be selected instead.
Note that this is only carried out for **connected atoms**, unlike when `Select`⇒`Invert Selection` is used.

**Select all atoms** using the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>A</kbd>.

**Clear the selection** by **right-clicking** in an empty part of the view pane or using the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd>.

:::{tip}
The keyboard shortcuts for select/deselect are always available, not only when the Selection Tool is the currently selected tool.
:::

:::{warning}
A known bug means that right-clicking to clear the selection does not work on some systems. A triple-left-click on empty space or a left-click on any currently selected atom should do the trick instead.
:::

## Pane options

Apply Color
: Pick a color and apply it to the currently selected atoms.

  Clicking the colored rectangle will open a color picker.
  After choosing a color, click `OK` to apply it.

Change Layer
: Move the selected atoms to a different layer.

  Putting parts of a molecule, or members of an ensemble, into different layers allows different visual settings to be applied to different elements within the same ["Molecule"](panes-molecules) (what Avogadro calls a file).
  
  See [Layers](panes-layers) for more information on how to use them.
