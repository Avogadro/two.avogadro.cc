(menus-crystal-menu)=

# Crystal Menu

The crystal menu contains many features useful for manipulating unit cells and crystal structures.

Import Crystal from Clipboard
: Open a dialog that allows you to import crystal structures from copied text. Supports multiple file formats (defaults to POSCAR).

Add Unit Cell
: Add a unit cell to the current document and open the [Unit Cell Editor](unit-cell-editor). (only if there is not a unit cell)

:::{note}
The following options are only available if the document has a unit cell.
:::

Remove Unit Cell
: Remove the unit cell from the current document.

Edit Unit Cell
: Open the [Unit Cell Editor](unit-cell-editor).

Fill Unit Cell
: Populate the unit cell, including translationally equivalent atoms. See [Translational Equivalence](translational-equivalence) for more information.

Fill Translational Cell
: Populate the unit cell, not including translationally equivalent atoms. See [Translational Equivalence](translational-equivalence) for more information.

Wrap Atoms to Unit Cell
: Take all atoms outside the unit cell and translate them into their equivalent position inside the unit cell.

Rotate to Standard Orientation
: Rotate the unit cell such that the cell matrix is in Hermite Normal Form.

Scale Cell Volume
: Apply a uniform scaling to the unit cell, and optionally translate the atoms as well.

Build Supercell
: Create a supercell using the current cell as the base unit cell.

Reduce Cell (Niggli)
: Perform a Niggli reduction on the current unit cell.

Plot Theoretical XRD Pattern
: Plot a theoretical x-ray diffraction pattern.

:::{warning}
If you get an error regarding a missing genXrdPattern executable, you can try to download the executable from [the GitHub repository](https://github.com/psavery/genXrdPattern/releases) and setting the `GENXRDPATTERN_EXECUTABLE` environment variable.
:::

Space Group
: See [Space Group Menu](space-group-menu)

Plot Pair Distribution Function
: Plot the [pair distribution function](https://en.wikipedia.org/wiki/Pair_distribution_function) for the current crystal.


(unit-cell-editor)=
## Unit Cell Editor

The unit cell editor is used for manipulating the unit cell.

```{figure} /_static/menus/crystal-menu/pd_unit_cell_editor.png
:alt: Cell parameters for Palladium
:align: center
:height: 480px
:class: dark-light
```

At the top of the unit cell editor are the lattice parameters $A$, $B$, $C$, $\alpha$, $\beta$, and $\gamma$. These either used to calculate the cell matrix, or can be calculated from the cell matrix. Below this is the cell matrix, which contains the three 3D lattice vectors, $\textbf{a}_i = (a^x_i, a^y_i, a^z_i)$ that make up the cell matrix (denoted here as $\mathbb{A}$). Below the cell matrix is the fractional matrix, which is the inverse of the unit cell matrix (denoted $\mathbb{A}^{-1}$). Together, the product of these matrices yields the identity matrix ($\mathbb{I}$),
```{math}
\mathbb{A}\mathbb{A}^{-1}=\mathbb{I}
```

The fractional matrix can be used to transform atoms from their normal 3D coordinates (denoted $r_i$) into what are called *fractional coordinates* (denoted $r^{\text{frac}}_i$), which can then be turned back into their normal coordinates by multiplying by the cell matrix.
```{math}
\mathbb{A}^{-1}\cdot r_i &= r^{\text{frac}}_i \\
\mathbb{A}\cdot r^{\text{frac}}_i &= r_i
```

At the bottom of the unit cell editor is an option to transform the atoms with the unit cell. This will keep your atom positions at the same *fractional coordinates*, while their normal 3D coordinates are shifted and scaled by the new unit cell. The remaining buttons at the bottom will either apply your changes, revert your most recent change, or hide/close the unit cell editor.

(translational-equivalence)=
## Translational Equivalence

A common tripping hazard when displaying crystal structures is the display of what are called *translationally equivalent atoms*. These are defined as atoms in a crystal structure which are separated by an integral translation along the lattice vectors. While this might seem complex at first, it can be very simply defined and shown, which we will do here.

For a mathematical description, imagine a unit cell with the following cell matrix (denoted $\mathbb{A}$):
```{math}
\mathbb{A} =
\begin{pmatrix}
a^x_1 & a^y_1 & a^z_1 \\
a^x_2 & a^y_2 & a^z_2 \\
a^x_3 & a^y_3 & a^z_3
\end{pmatrix}
```
The individual lattice vectors $\textbf{a}_i = (a^x_i, a^y_i, a^z_i)$, or their integer multiples (e.g. $1\times\textbf{a}_i$, $-1\times\textbf{a}_i$, $2\times\textbf{a}_i$, $-2\times\textbf{a}_i$, etc.), can be used to *translate* or *slide* atoms around in space. To find the *translationally equivalent* atoms in a unit cell, you can take all of the atoms in the cell, apply positive ($+$) or negative ($-$) translations (possibly with an integer multiplier) with the lattice vectors, and then remove all of the atoms which are related by that translation.

As a visual demonstration of this, consider a the conventional unit cell of Palladium, which has a Face-Centered Cubic crystal structure. Below we show the unit cell produced with the `Fill Unit Cell` command and the unit cell matrix ($\mathbb{A}$ from above):

::::{tab-set}
:::{tab-item} Unit Cell
```{image} /_static/menus/crystal-menu/pd_conventional_cell_dark.png
:alt: Filled palladium unit cell
:align: center
:height: 300px
:class: only-dark
```
```{image} /_static/menus/crystal-menu/pd_conventional_cell_light.png
:alt: Filled palladium unit cell
:align: center
:height: 300px
:class: only-light
```
:::
:::{tab-item} Cell Matrix
```{image} /_static/menus/crystal-menu/pd_unit_cell_editor.png
:alt: Cell parameters for Palladium
:align: center
:height: 300px
:class: dark-light
```
:::
::::

Applying transformations to the atoms on the corners of the unit cell (highlighted in blue here)

```{figure} /_static/menus/crystal-menu/pd_filled_highlighted_corners_dark.png
:alt: Filled palladium unit cell with the corner atoms highlighted
:align: center
:height: 300px
:class: only-dark
```
```{figure} /_static/menus/crystal-menu/pd_filled_highlighted_corners_light.png
:alt: Filled palladium unit cell with the corner atoms highlighted
:align: center
:height: 300px
:class: only-light
```

The coordinates of these atoms are (in no particular order),
| Atom Number | X Pos. (Å) | Y Pos. (Å) | Z Pos. (Å) |
| :---------: | :--------- | :--------- | :--------- |
|      1      |   0.0000   |   0.0000   |   0.0000   |
|      2      |   3.8898   |   0.0000   |   0.0000   |
|      3      |   0.0000   |   3.8898   |   0.0000   |
|      4      |   0.0000   |   0.0000   |   3.8898   |
|      5      |   3.8898   |   3.8898   |   0.0000   |
|      6      |   3.8898   |   0.0000   |   3.8898   |
|      7      |   0.0000   |   3.8898   |   3.8898   |
|      8      |   3.8898   |   3.8898   |   3.8898   |

Using the lattice vectors
```{math}
\textbf{a}_1 &= (3.8898,\; 0.0000,\; 0.0000) \\
\textbf{a}_2 &= (0.0000,\; 3.8898,\; 0.0000) \\
\textbf{a}_3 &= (0.0000,\; 0.0000,\; 3.8898)
```
we can subtract them from the positions of atoms 2-4 (denoted $r_i$) and see that they all are *translationally equivalent* to atom 1:
```{math}
r_2 - \textbf{a}_1 = (3.8898, 0.0000, 0.0000) - (3.8898, 0.0000, 0.0000) = (0, 0, 0) \\
r_3 - \textbf{a}_2 = (0.0000, 3.8898, 0.0000) - (0.0000, 3.8898, 0.0000) = (0, 0, 0) \\
r_4 - \textbf{a}_3 = (0.0000, 0.0000, 3.8898) - (0.0000, 0.0000, 3.8898) = (0, 0, 0)
```

The remaining corner atoms are a simple extension of this, but with multiple translations:
```{math}
&r_5 - \textbf{a}_1 - \textbf{a}_2 &= (0, 0, 0) \\
&r_6 - \textbf{a}_1 - \textbf{a}_3 &= (0, 0, 0) \\
&r_7 - \textbf{a}_2 - \textbf{a}_3 &= (0, 0, 0) \\
&r_8 - \textbf{a}_1 - \textbf{a}_2 - \textbf{a}_3 &= (0, 0, 0)
```

Now moving on to the face atoms, again highlighted in the image below.

```{figure} /_static/menus/crystal-menu/pd_filled_highlighted_faces_dark.png
:alt: Filled unit cell of palladium with the atoms on the faces highlighted
:align: center
:height: 300px
:class: only-dark
```
```{figure} /_static/menus/crystal-menu/pd_filled_highlighted_faces_light.png
:alt: Filled unit cell of palladium with the atoms on the faces highlighted
:align: center
:height: 300px
:class: only-light
```


Their coordinates are listed below (with numbering starting from 9 to avoid confusion with the corner atoms):
| Atom Number | X Pos. (Å) | Y Pos. (Å) | Z Pos. (Å) |
| :---------: | :--------- | :--------- | :--------- |
|      1      |   0.0000   |   0.0000   |   0.0000   |
|      9      |   0.0000   |   1.9449   |   1.9449   |
|     10      |   1.9449   |   0.0000   |   1.9449   |
|     11      |   1.9449   |   1.9449   |   0.0000   |
|     12      |   3.8898   |   1.9449   |   1.9449   |
|     13      |   1.9449   |   3.8898   |   1.9449   |
|     14      |   1.9449   |   1.9449   |   3.8898   |

One thing to note right off the bat is that none of the face atoms will be *translationally equivalent* to atom 1 as they all have components which are not equal to a lattice vector multiplied by an integer. For example, atom 9 can not be translated into atom 1
```{math}
r_9 - \textbf{a}_2 - \textbf{a}_3 = (0.0000, -1.9449, -1.9449)
```

As such, we know that some of these atoms will need to remain in the *translational unit cell*. Applying the same formulas from above, we can see that atoms 12, 13, and 14 can be translated by the lattice vectors into atoms 9, 10, and 11.
```{math}
&r_{12} - \textbf{a}_1 &= (0.0000,\; 1.9449,\; 1.9449) &= r_9 \\
&r_{13} - \textbf{a}_2 &= (1.9449,\; 0.0000,\; 1.9449) &= r_{10} \\
&r_{14} - \textbf{a}_3 &= (1.9449,\; 1.9449,\; 0.0000) &= r_{11}
```

Thus, we know that the *translational unit cell* contains only atoms 1, 9, 10, and 11. Using Avogadro 2's `Fill Translation Cell` command, we see that this is the exact unit cell that we get:

```{figure} /_static/menus/crystal-menu/pd_translation_cell_dark.png
:alt: Translational unit cell of palladium
:align: center
:height: 300px
:class: only-dark
```
```{figure} /_static/menus/crystal-menu/pd_translation_cell_light.png
:alt: Translational unit cell of palladium
:align: center
:height: 300px
:class: only-light
```

(space-group-menu)=
## Space Group Menu

The Space Group dropdown supplies tools for interacting with the [Space Group Library (Spglib)](https://spglib.readthedocs.io/en/stable/index.html) through Avogadro 2.

Perceive Space Group
: Determine the space group of the current crystal structure.

Reduce to Primitive
: Reduce the current unit cell to the primitive unit cell.

Conventionalize Cell
: Take a primitive unit cell and turn it into its conventional form.

:::::{dropdown} Primitive vs. Conventional Cell
:color: info
:icon: image

::::{tab-set}

:::{tab-item} Conventional Unit Cell
```{image} /_static/menus/crystal-menu/pd_conventional_cell_dark.png
:alt: Conventional unit cell of palladium
:align: center
:height: 300px
:class: only-dark
```
```{image} /_static/menus/crystal-menu/pd_conventional_cell_light.png
:alt: Conventional unit cell of palladium
:align: center
:height: 300px
:class: only-light
```
:::

:::{tab-item} Primitive Unit Cell
```{image} /_static/menus/crystal-menu/pd_primitive_cell_dark.png
:alt: Primitive unit cell of palladium
:align: center
:height: 300px
:class: only-dark
```
```{image} /_static/menus/crystal-menu/pd_primitive_cell_light.png
:alt: Primitive unit cell of palladium
:align: center
:height: 300px
:class: only-light
```
:::

::::

:::::

Symmetrize
: Take a cell that is not perfectly symmetric, reduce it to its primitive form, and idealize it.

Reduce to Asymmetric Unit
: Reduce the unit cell to all atoms which can not be represented by the point group's symmetry operations.

Set Tolerance
: Set the default tolerance for the other operations in the menu.
