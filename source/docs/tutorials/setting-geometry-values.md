(tutorials-setting-geometry-values)=

# Setting a Bond Length, Angle or Dihedral

Sometimes you want a bond length, angle or dihedral at an exact value: a C–C bond at 1.54 Å, a water angle at 104.5°, or a torsion at 60° to build a *gauche* conformer before a scan. Avogadro has several ways to do this. This tutorial walks through each one, so you can pick the one that suits your task.

| Method | Best for |
| --- | --- |
| [Measure Tool](with-the-measure-tool) | Quickly setting one value between atoms you click on |
| [Property tables](with-the-property-tables) | Finding and setting a value in a list of every bond, angle or torsion |
| [Z-Matrix Editor](with-the-z-matrix-editor) | Setting many values, or building a geometry from internal coordinates |
| [Bond-Centric Manipulation Tool](with-the-bond-centric-manipulation-tool) | Adjusting by eye with the mouse, while watching the value |

In every case, Avogadro moves only part of the molecule. One end stays fixed, and the other end moves along with everything attached to it on its side of the bond, so the rest of the geometry is preserved.

As an example, build butane (e.g., `Build` ⇒ `Insert` ⇒ `SMILES…` and type `CCCC`) and set the C–C–C–C dihedral to 60°.

(with-the-measure-tool)=

## With the Measure Tool

```{tip} **New in 2.1**
Values can now be typed directly into the Measure tool.
```

1. Choose the [Measure Tool](tools-measure-tool) (<kbd>Ctrl</kbd>+<kbd>8</kbd>).
2. Click the atoms in order. Click two atoms for a distance, three for an angle (the second atom is the vertex), or four for a dihedral. For the butane example, click the four carbons from one end to the other.
3. The Tool pane shows each distance, angle and dihedral that the atoms define. Type the new value (e.g., `60` in **Dihedral 1–2–3–4**) and press <kbd>Enter</kbd>.

% TODO(screenshot): /_static/tutorial-set-dihedral-measure.png -- butane with the four carbons picked, Tool pane showing Dihedral 1–2–3–4 = 60°

Atom #1 stays fixed, and the atoms move toward the last atom you clicked. If an edit can't be made, for example because the dihedral is around a bond in a ring, a message explains why and nothing moves. See {ref}`measure-tool-editing` for details.

(with-the-property-tables)=

## With the Property Tables

The property tables list every bond, angle and torsion in the molecule:

- `Analyze` ⇒ `Properties` ⇒ `Bond Properties…`
- `Analyze` ⇒ `Properties` ⇒ `Angle Properties…`
- `Analyze` ⇒ `Properties` ⇒ `Torsion Properties…`

1. Open the table you need. For the butane example, open the torsion table.
2. Click a row to find the right one. The atoms in that row are selected in the 3D view.
3. Double-click the value (the **Length (Å)** or **Angle (°)** column), type the new value and press <kbd>Enter</kbd>.

% TODO(screenshot): /_static/tutorial-set-dihedral-table.png -- the Torsion Properties table with the C-C-C-C row being edited

:::{tip}
Click a column header to sort the table, for example to find the longest bond. Right-click a row to add a constraint that holds the value fixed during a later optimization.
:::

(with-the-z-matrix-editor)=

## With the Z-Matrix Editor

```{tip} **New in 2.1**
The Z-Matrix Editor is new in version 2.1.
```

The {ref}`Z-Matrix Editor <building-molecules-zmatrix-editor>` shows every atom as a distance, angle and dihedral to atoms placed before it. It's the quickest way to set many values in a row.

1. Choose `Build` ⇒ `Z-Matrix Editor…`.
2. Find the row for the atom you want to move. Selecting atoms in the 3D view highlights their rows.
3. Double-click the **Distance**, **Angle** or **Dihedral** cell, type the new value and press <kbd>Enter</kbd>.

The atom in that row moves, along with the part of the molecule attached to it. If the row isn't measured against the atoms you want, type different atom numbers into its reference columns first.

(with-the-bond-centric-manipulation-tool)=

## With the Bond-Centric Manipulation Tool

If you don't need an exact number, the [Bond-Centric Manipulation Tool](tools-bond-centric-manipulation-tool) (<kbd>Ctrl</kbd>+<kbd>6</kbd>) lets you click a bond and drag its atoms to change the bond length or the angles around it. The values are shown in the view as you drag. Use one of the methods above to type in an exact value afterward.

## Keeping the Value During Optimization

A geometry optimization will move the value you set back toward its preferred value. To keep it:

- Right-click the row in the property table and choose **Constrain Bond**, **Constrain Angle** or **Constrain Torsion**, or
- Right-click the value in the Z-Matrix Editor and choose **Constrain Distance**, **Constrain Angle** or **Constrain Dihedral**.

Then optimize (`Extensions` ⇒ `Optimize Geometry`, <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>O</kbd>). The rest of the molecule relaxes while the constrained value stays put. See {ref}`optimize-constraints`.

## See Also

- {ref}`tools-measure-tool` – Measure and edit distances, angles and dihedrals
- {ref}`building-molecules-zmatrix-editor` – Edit the molecule as a z-matrix
- [Properties](panes-properties) – The property tables
- {ref}`optimize-constraints` – Hold values fixed during optimization
