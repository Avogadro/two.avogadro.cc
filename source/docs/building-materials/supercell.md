(building-materials-supercell)=

# Building a Supercell

A common task in solid state simulations is the use of supercells for calculating various properties such as phonon modes. Avogadro's supercell builder in the [Crystal Menu](menus-crystal-menu) can be used to create supercells with ease.

To start, import a crystal with **File ⇒ Import ⇒ Crystal...** and import a crystal structure. This guide will use halite (NaCl).

```{figure} /_static/building-materials/import_halite.png
:alt: Picture of the import menu showing halite
:align: center
:class: dark-light
```

```{figure} /_static/building-materials/halite_basic_cell_light.png
:alt: Picture of the unfilled halite unit cell
:align: center
:height: 300px
:class: only-light
```
```{figure} /_static/building-materials/halite_basic_cell_dark.png
:alt: Picture of the unfilled halite unit cell
:align: center
:height: 300px
:class: only-dark
```

Once you've imported the crystal, go to **Crystal ⇒ Fill Translation Cell** to fill only the [translationally inequivalent atoms](translational-equivalence), which is most suitable for use in a calculation.

```{figure} /_static/building-materials/halite_translation_cell_light.png
:alt: Picture of the translation-inequivalent filled halite unit cell
:align: center
:height: 300px
:class: only-light
```
```{figure} /_static/building-materials/halite_translation_cell_dark.png
:alt: Picture of the translation-inequivalent filled halite unit cell
:align: center
:height: 300px
:class: only-dark
```

After this, you can go to **Crystal ⇒ Build Supercell...** which will open the supercell builder.

```{figure} /_static/building-materials/supercell_dialog.png
:alt: Picture of the supercell builder
:align: center
:class: dark-light
```

In this instance, a 2×2×2 supercell is used, but Avogadro 2 is capable of handling very large systems, so don't feel limited to this size. Hit **OK**, to build the supercell, and you're ready for a calculation!

::::{tab-set}

:::{tab-item} Single Unit Cell
```{image} /_static/building-materials/halite_translation_cell_small_light.png
:alt: Zoomed-out view of the single halite translation cell
:align: center
:height: 480px
:class: only-light
```
```{image} /_static/building-materials/halite_translation_cell_small_dark.png
:alt: Zoomed-out view of the single halite translation cell
:align: center
:height: 480px
:class: only-dark
```
:::

:::{tab-item} Supercell
```{image} /_static/building-materials/halite_translation_supercell_light.png
:alt: 2×2×2 supercell of halite.
:align: center
:height: 480px
:class: only-light
```
```{image} /_static/building-materials/halite_translation_supercell_dark.png
:alt: 2×2×2 supercell of halite.
:align: center
:height: 480px
:class: only-dark
```
:::

::::

## Creating a Surface

The supercell builder can also be used for basic slab creation. Here we will demonstrate the creation of a nanopore in a graphene sheet using the supercell builder.

## See Also

- {ref}`building-materials-crystal-slab` – Create crystal surface slabs for specific Miller planes
- {ref}`building-materials-crystal-symmetry` – Perceive space groups from crystal coordinates
- {ref}`building-materials-polymer-unit-cell` – Build polymer unit cells for periodic calculations
