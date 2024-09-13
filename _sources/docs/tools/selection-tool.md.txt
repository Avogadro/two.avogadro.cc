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

**Double-left-click** on an atom to instantly **select all connected atoms**.
"Connected" atoms are any that can be traced to the clicked atom through bonds, including over multiple bonds i.e. the whole molecule.

![An entire molecule selected after clicking on one of its constituent atoms.](../../_static/tutorial-select-all.png){height=300px align=center}

:::{tip}
Use `Select`⇒`Enlarge Selection` to increase the selection from an atom to only its immediate neighbors rather than the whole molecule.
:::

Holding <kbd>Shift</kbd> or <kbd>Ctrl</kbd> while doing the above actions modifies their behaviour.

The effects of the modifier keys are best summarized in the table below:

|                         | with no modifier                    | with <kbd>Shift</kbd>                           | with <kbd>Ctrl</kbd>                                                                  |
| ---                     | ---                                 | ---                                             | ---                                                                                   |
| *general effect*        | *select*                            | *add*                                           | *toggle/invert*                                                                       |
| **click**               | Atom is selected.                   | Atom is added to selection.                     | Atom is toggled between selected and unselected.                                      |
| **click and drag**      | All atoms within box are selected.  | All atoms within box are added to selection.    | Unselected atoms within box are selected, but selected atoms are deselected.          | 
| **double-click**        | Whole molecule is selected.         | Whole molecule is added to selection.           | Unselected atoms within the molecule are selected, but selected atoms are deselected. |
| *effect on other atoms* | Other atoms are deselected.         | All previously selected atoms remain selected.  | Other atoms remain as they were.                                                      |

Note that while <kbd>Ctrl</kbd> and **double-left-click** inverts the selection, this only affects **connected atoms**, whereas when `Select`⇒`Invert Selection` is used, the inversion applies to all atoms.

**Select all atoms** using the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>A</kbd>.

**Clear the selection** by **right-clicking** in an empty part of the view pane or using the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd>.

:::{tip}
The keyboard shortcuts for select/deselect all are always available, not only when the Selection Tool is the currently selected tool.
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
