(tools-keyboard-shortcuts)=

# Keyboard Shortcuts

This page collects all keyboard shortcuts in one place for quick reference. For more detail on each tool, follow the cross-references.

## Switching Tools

Tools can be selected by pressing <kbd>Ctrl</kbd> and the corresponding number key.

| Shortcut | Tool |
|----------|------|
| <kbd>Ctrl</kbd>+<kbd>1</kbd> | {ref}`Navigation Tool <tools-navigation-tool>` |
| <kbd>Ctrl</kbd>+<kbd>2</kbd> | {ref}`Draw Tool <tools-draw-tool>` |
| <kbd>Ctrl</kbd>+<kbd>3</kbd> | {ref}`Template Tool <tools-template-tool>` |
| <kbd>Ctrl</kbd>+<kbd>4</kbd> | {ref}`Selection Tool <tools-selection-tool>` |
| <kbd>Ctrl</kbd>+<kbd>5</kbd> | {ref}`Manipulation Tool <tools-manipulation-tool>` |
| <kbd>Ctrl</kbd>+<kbd>6</kbd> | {ref}`Bond-Centric Manipulation Tool <tools-bond-centric-manipulation-tool>` |
| <kbd>Ctrl</kbd>+<kbd>7</kbd> | {ref}`AutoOptimization Tool <tools-autoopt-tool>` |
| <kbd>Ctrl</kbd>+<kbd>8</kbd> | {ref}`Measure Tool <tools-measure-tool>` |
| <kbd>Ctrl</kbd>+<kbd>9</kbd> | {ref}`Animation Tool <tools-animation-tool>` |

The {ref}`Align Tool <tools-align-tool>` and {ref}`Label Tool <tools-label-tool>` do not currently have tool-switching shortcuts.

## Global Shortcuts

These shortcuts work regardless of which tool is currently selected.

| Shortcut | Action |
|----------|--------|
| <kbd>Ctrl</kbd>+<kbd>A</kbd> | Select all atoms |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd> | Deselect all atoms |
| <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>O</kbd> | {ref}`Optimize geometry <calculations-optimization>` |

## Navigation

The {ref}`Navigation Tool <tools-navigation-tool>` responds to mouse and keyboard input. Many of these actions also work while other tools are active, as long as the action is not already defined for that tool.

### Mouse

| Action | Effect |
|--------|--------|
| Left-click + drag | Rotate (x/y axes) |
| Middle-click + drag | Rotate (z-axis) |
| Right-click + drag | Pan (x/y) |
| Scroll wheel | Zoom |
| Middle double-click | Reset camera |
|--------|--------|
| <kbd>Alt / Option</kb> Left-click + drag | Rotate (x/y axes) |
| <kbd>Shift</kbd> + left-click + drag | Rotate (z-axis) |
| <kbd>Ctrl</kbd> + left-click + drag | Pan (x/y) |

If you do not have a multi-button mouse or touch-pad, you can use the modifier keys <kbd>Alt</kbd> or <kbd>Shift</kbd> or <kbd>Ctrl</kbd> for these actions.

### Keyboard

Three equivalent sets of directional keys are supported: **Arrow keys**, **WASD**, and **HJKL**.

- <kbd>&uarr;</kbd> = <kbd>W</kbd> = <kbd>K</kbd> (referred to as <kbd>up</kbd> below)
- <kbd>&darr;</kbd> = <kbd>S</kbd> = <kbd>J</kbd> (<kbd>down</kbd>)
- <kbd>&larr;</kbd> = <kbd>A</kbd> = <kbd>H</kbd> (<kbd>left</kbd>)
- <kbd>&rarr;</kbd> = <kbd>D</kbd> = <kbd>L</kbd> (<kbd>right</kbd>)

| Shortcut | Action |
|----------|--------|
| Directional keys | Rotate (x/y axes) |
| <kbd>Shift</kbd> + <kbd>left</kbd> / <kbd>right</kbd> | Rotate (z-axis) |
| <kbd>Ctrl</kbd> + directional keys | Pan (x/y) |
| <kbd>Shift</kbd> + <kbd>up</kbd> / <kbd>down</kbd> | Zoom |

Hold <kbd>Alt</kbd> together with any keyboard navigation action to increase the step size.

:::{warning}
<kbd>Ctrl</kbd>+<kbd>W</kbd>, <kbd>Ctrl</kbd>+<kbd>A</kbd>, and <kbd>Ctrl</kbd>+<kbd>S</kbd> are mapped to other functions and cannot be used for panning. Use the arrow keys or HJKL instead.
:::

## Draw Tool

See {ref}`tools-draw-tool` for full details.

| Shortcut | Action |
|----------|--------|
| Type element symbol (e.g. <kbd>O</kbd>, <kbd>A</kbd><kbd>s</kbd>) | Change current element |
| <kbd>1</kbd> | Single bond order |
| <kbd>2</kbd> | Double bond order |
| <kbd>3</kbd> | Triple bond order |

## Selection Tool

See {ref}`tools-selection-tool` for full details.

| Modifier | Click | Click + drag | Double-click |
|----------|-------|-------------|--------------|
| *(none)* | Select atom | Marquee select | Select molecule |
| <kbd>Shift</kbd> | Add to selection | Add to selection | Add molecule to selection |
| <kbd>Ctrl</kbd> | Toggle atom | Invert in box | Invert in molecule |

## Template Tool

See {ref}`tools-template-tool` for full details and the complete {ref}`shortcut tables <template-tool-shortcuts>`.

### Tab Navigation

| Key | Action |
|-----|--------|
| <kbd>&larr;</kbd> or <kbd>[</kbd> | Previous tab |
| <kbd>&rarr;</kbd> or <kbd>]</kbd> | Next tab |

### Centers Tab

**Element:** Type any element symbol (e.g. <kbd>F</kbd><kbd>e</kbd>, <kbd>C</kbd><kbd>u</kbd>, <kbd>N</kbd><kbd>i</kbd>).

| Key | Action |
|-----|--------|
| <kbd>+</kbd> | Increase formal charge |
| <kbd>-</kbd> | Decrease formal charge |

**Coordination geometry:**

| Key | Geometry |
|-----|----------|
| <kbd>1</kbd> | Linear (terminal) |
| <kbd>2</kbd> | Linear |
| <kbd>3</kbd> | Trigonal planar |
| <kbd>4</kbd> | Tetrahedral |
| <kbd>4</kbd><kbd>4</kbd> | Square planar |
| <kbd>5</kbd> | Trigonal bipyramidal |
| <kbd>5</kbd><kbd>5</kbd> | Square pyramidal |
| <kbd>6</kbd> | Octahedral |
| <kbd>6</kbd><kbd>6</kbd> | Trigonal prismatic |
| <kbd>7</kbd> | Pentagonal bipyramidal |
| <kbd>8</kbd> | Square antiprismatic |

### Ligands Tab

**Monodentate:**

| Key | Ligand |
|-----|--------|
| <kbd>a</kbd> or <kbd>o</kbd> | Aqua (H₂O) |
| <kbd>co</kbd> | Carbonyl (CO) |
| <kbd>cn</kbd> | Cyano (CN⁻) |
| <kbd>n</kbd> | Ammine (NH₃) |
| <kbd>p</kbd> | Phosphine (PH₃) |
| <kbd>pyr</kbd> | Pyridyl |
| <kbd>s</kbd> | Thiol (SH⁻) |

**Bidentate:**

| Key | Ligand |
|-----|--------|
| <kbd>acac</kbd> | Acetylacetonate |
| <kbd>bpy</kbd> | Bipyridine |
| <kbd>dmg</kbd> | Dimethylglyoxime |
| <kbd>dmpe</kbd> | 1,2-bis(dimethylphosphino)ethane |
| <kbd>dppe</kbd> | 1,2-bis(diphenylphosphino)ethane |
| <kbd>en</kbd> | Ethylenediamine |
| <kbd>ox</kbd> | Oxalate |
| <kbd>phen</kbd> | Phenanthroline |

**Tridentate and higher:**

| Key | Ligand |
|-----|--------|
| <kbd>tpy</kbd> | Terpyridine (tridentate) |
| <kbd>pc</kbd> | Phthalocyanine (tetradentate) |
| <kbd>por</kbd> | Porphin (tetradentate) |
| <kbd>sal</kbd> | Salen (tetradentate) |
| <kbd>edta</kbd> | EDTA (hexadentate) |

**Haptic:**

| Key | Ligand |
|-----|--------|
| <kbd>e</kbd><kbd>2</kbd> | η²-Ethylene |
| <kbd>e</kbd><kbd>3</kbd> | η³-Allyl |
| <kbd>e</kbd><kbd>4</kbd> | η⁴-Cyclooctadiene |
| <kbd>e</kbd><kbd>5</kbd> or <kbd>c</kbd><kbd>p</kbd> | η⁵-Cyclopentadienyl |
| <kbd>e</kbd><kbd>6</kbd> | η⁶-Benzene |

### Groups Tab

**Alkyl chains:**

| Key | Group |
|-----|-------|
| <kbd>c</kbd> or <kbd>c1</kbd> | Methyl |
| <kbd>c2</kbd> | Ethyl |
| <kbd>c3</kbd> – <kbd>c9</kbd> | Propyl – Nonyl |
| <kbd>c0</kbd> | Decyl |

**Cycloalkyl** (uppercase <kbd>C</kbd>):

| Key | Group |
|-----|-------|
| <kbd>C3</kbd> – <kbd>C9</kbd> | Cyclopropane – Cyclononane |
| <kbd>C</kbd><kbd>0</kbd> | Cyclodecane |

**Branched alkyl:**

| Key | Group |
|-----|-------|
| <kbd>I</kbd> | Iso-propyl |
| <kbd>K</kbd> or <kbd>c</kbd><kbd>m</kbd> | tert-Butyl |

**Common functional groups:**

| Key | Group |
|-----|-------|
| <kbd>a</kbd> | Phenyl |
| <kbd>C</kbd> or <kbd>co2</kbd> | Carboxylate |
| <kbd>cn</kbd> | Nitrile |
| <kbd>co</kbd> | Aldehyde |
| <kbd>E</kbd> | Ester |
| <kbd>F</kbd> | Trifluoromethyl |
| <kbd>N</kbd> or <kbd>no2</kbd> | Nitro |
| <kbd>om</kbd> | Methoxy |
| <kbd>P</kbd> or <kbd>po3</kbd> | Phosphate |
| <kbd>S</kbd> or <kbd>so3</kbd> | Sulfonate |

**Protecting groups:**

| Key | Group |
|-----|-------|
| <kbd>boc</kbd> | BOC |
| <kbd>cbz</kbd> | CBZ |
| <kbd>fmoc</kbd> | FMOC |
| <kbd>ms</kbd> | Mesyl |
| <kbd>tos</kbd> or <kbd>ts</kbd> | Tosyl |
| <kbd>tr</kbd> | Trityl |
| <kbd>troc</kbd> | TROC |

:::{tip}
Template Tool shortcuts are case-sensitive. For example, <kbd>c</kbd><kbd>6</kbd> selects hexyl while <kbd>C</kbd><kbd>6</kbd> selects cyclohexane.
:::

:::{note}
Multi-character shortcuts have a 2-second timeout. The buffer clears automatically after 5 characters if no match is found.
:::

## Align Tool

See {ref}`tools-align-tool` for full details.

| Key | Action |
|-----|--------|
| <kbd>x</kbd> | Set alignment to X axis |
| <kbd>y</kbd> | Set alignment to Y axis |
| <kbd>z</kbd> | Set alignment to Z axis |

## Label Tool

See {ref}`tools-label-tool` for full details.

| Key | Action |
|-----|--------|
| <kbd>Enter</kbd> | Confirm label |
