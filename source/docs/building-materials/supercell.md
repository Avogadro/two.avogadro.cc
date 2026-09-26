(building-materials-supercell)=

# Building a Supercell

A common task in solid state simulations is the use of supercells for calculating various properties such as phonon modes.
Avogadro's supercell builder in the [Crystal Menu](menus-crystal-menu) can be used to create supercells with ease.

To start, import a crystal with **File ⇒ Import ⇒ Crystal...** and import a crystal structure.
This guide will use halite (NaCl).

```{figure} /_static/building-materials/supercell/import_halite.png
:alt: Picture of the import menu showing halite
:align: center
:height: 300px
:class: dark-light
```

```{figure} /_static/building-materials/supercell/halite_basic_cell_light.png
:alt: Picture of the unfilled halite unit cell
:align: center
:height: 300px
:class: only-light
```
```{figure} /_static/building-materials/supercell/halite_basic_cell_dark.png
:alt: Picture of the unfilled halite unit cell
:align: center
:height: 300px
:class: only-dark
```

Once you've imported the crystal, go to **Crystal ⇒ Fill Translation Cell** to fill only the [translationally inequivalent atoms](translational-equivalence), which is most suitable for use in a calculation.

```{figure} /_static/building-materials/supercell/halite_translation_cell_light.png
:alt: Picture of the translation-inequivalent filled halite unit cell
:align: center
:height: 300px
:class: only-light
```
```{figure} /_static/building-materials/supercell/halite_translation_cell_dark.png
:alt: Picture of the translation-inequivalent filled halite unit cell
:align: center
:height: 300px
:class: only-dark
```

After this, you can go to **Crystal ⇒ Build Supercell...** which will open the supercell builder.

```{figure} /_static/building-materials/supercell/supercell_dialog.png
:alt: Picture of the supercell builder
:align: center
:class: dark-light
```

In this instance, a 2×2×2 supercell is used, but Avogadro 2 is capable of handling very large systems, so don't feel limited to this size.
Hit **OK**, to build the supercell, and you're ready for a calculation!

::::{tab-set}

:::{tab-item} Single Unit Cell
```{image} /_static/building-materials/supercell/halite_translation_cell_small_light.png
:alt: Zoomed-out view of the single halite translation cell
:align: center
:height: 480px
:class: only-light
```
```{image} /_static/building-materials/supercell/halite_translation_cell_small_dark.png
:alt: Zoomed-out view of the single halite translation cell
:align: center
:height: 480px
:class: only-dark
```
:::

:::{tab-item} Supercell
```{image} /_static/building-materials/supercell/halite_translation_supercell_light.png
:alt: 2×2×2 supercell of halite.
:align: center
:height: 480px
:class: only-light
```
```{image} /_static/building-materials/supercell/halite_translation_supercell_dark.png
:alt: 2×2×2 supercell of halite.
:align: center
:height: 480px
:class: only-dark
```
:::

::::

## Creating a Surface

The supercell builder can also be used for basic slab creation.
Here we will demonstrate how one might create a nanopore in a graphene sheet using the supercell builder.

First start by importing the crystal structure of graphite, which is simply just stacked graphene sheets.

```{figure} /_static/building-materials/supercell/import_graphite.png
:alt: Picture of the import menu showing graphite
:align: center
:height: 480px
:class: dark-light
```

Next, use **Crystal ⇒ Fill Translation Cell** to remove the redundant atoms, after which you should be left with a structure that looks like the one below.

```{figure} /_static/building-materials/supercell/graphene_example/graphite_translation_cell_light.png
:alt: Picture of the translation cell of graphite
:align: center
:height: 300px
:class: only-light
```
```{figure} /_static/building-materials/supercell/graphene_example/graphite_translation_cell_dark.png
:alt: Picture of the translation cell of graphite
:align: center
:height: 300px
:class: only-dark
```

After this, we are going to build a 1-1-2 supercell and remove the atoms above and below the middle layer.
This will give us some vacuum padding on the top and bottom of our graphene sheet so that they don't interact with each other in a periodic calculation.

::::{tab-set}

:::{tab-item} Supercell Dialog
```{image} /_static/building-materials/supercell/graphite_112_supercell_dialog.png
:alt: 1-1-2 supercell dialog.
:align: center
:height: 480px
:class: dark-light
```
:::

:::{tab-item} Elongated Supercell
```{image} /_static/building-materials/supercell/graphene_example/graphite_112_supercell_light.png
:alt: The 1-1-2 graphite supercell.
:align: center
:height: 480px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_112_supercell_dark.png
:alt: The 1-1-2 graphite supercell.
:align: center
:height: 480px
:class: only-dark
```
:::

:::{tab-item} Atoms to delete
```{image} /_static/building-materials/supercell/graphene_example/graphite_112_supercell_selected_light.png
:alt: The 1-1-2 graphite supercell with the atoms above and below the middle selected.
:align: center
:height: 480px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_112_supercell_selected_dark.png
:alt: The 1-1-2 graphite supercell with the atoms above and below the middle selected.
:align: center
:height: 480px
:class: only-dark
```
:::

:::{tab-item} Resulting Supercell
```{image} /_static/building-materials/supercell/graphene_example/graphite_112_supercell_trimmed_light.png
:alt: The 1-1-2 graphite supercell with only the middle atoms remaining.
:align: center
:height: 480px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_112_supercell_trimmed_dark.png
:alt: The 1-1-2 graphite supercell with only the middle atoms remaining.
:align: center
:height: 480px
:class: only-dark
```
:::

::::

Now that we have our 1-1-2 supercell ready, we can proceed to creating the final 8-8-2 supercell for our nanopore defect.
Keep in mind that since we have already created the 1-1-2, we only need to put in 8-8-1 into the supercell builder dialog.

::::{tab-set}

:::{tab-item} Supercell Dialog
```{image} /_static/building-materials/supercell/graphite_882_supercell_dialog.png
:alt: 8-8-2 supercell dialog.
:align: center
:height: 300px
:class: dark-light
```
:::

:::{tab-item} 1-1-2 Supercell
```{image} /_static/building-materials/supercell/graphene_example/graphite_pre_supercell_topdown_light.png
:alt: The 1-1-2 graphene supercell.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_pre_supercell_topdown_dark.png
:alt: The 1-1-2 graphene supercell.
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 8-8-2 Supercell
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_light.png
:alt: The 8-8-2 graphene supercell
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_dark.png
:alt: The 8-8-2 graphene supercell
:align: center
:height: 300px
:class: only-dark
```
:::

::::

Now that we have our final size of supercell, we can start carving out the nanopore.
First, we are starting with a small set of 6 carbon atoms in the middle of the cell, which we will be deleting.
Next, replace the two pairs of carbon atoms jutting out into the new hole we have created with hydrogen atoms.
When you do this, be sure to delete the bond between the carbon atoms first so that Avogadro will automatically re-scale the bond lengths to be more appropriate.
Finally, replace the two pairs of carbon atoms that have unsatisfied octets (highlighted) with nitrogen atoms, and you're done!

::::{tab-set}

:::{tab-item} Start
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_selected_light.png
:alt: The 8-8-2 supercell with the atoms that will be deleted to make our nanopore.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_selected_dark.png
:alt: The 8-8-2 supercell with the atoms that will be deleted to make our nanopore.
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} Initial Pore
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_highlight_hydrogens_light.png
:alt: The 8-8-2 graphene supercell with the nanopore opened up and the next atoms to change highlighted.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_highlight_hydrogens_dark.png
:alt: The 8-8-2 graphene supercell with the nanopore opened up and the next atoms to change highlighted.
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} Replace with Hydrogen
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_highlight_nitrogens_light.png
:alt: The 8-8-2 graphene supercell with the hydrogens placed and the next atoms to change highlighted.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_highlight_nitrogens_dark.png
:alt: The 8-8-2 graphene supercell with the hydrogens placed and the next atoms to change highlighted.
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} Replace with Nitrogen
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_nitrogens_light.png
:alt: The 8-8-2 graphene supercell with the completed nitrogen-functionalized nanopore.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_nitrogens_dark.png
:alt: The 8-8-2 graphene supercell with the completed nitrogen-functionalized nanopore.
:align: center
:height: 300px
:class: only-dark
```
:::

::::

Now that you have the defect crafted, you can proceed to run calculations with it!
In [Jiang, Cooper, and Dai, 2009](https://doi.org/10.1021/nl9021946), calculations were run that indicated that porous graphene could be a highly selective membrane for gas separation.
Their work had them using a graphene cell with the exact same defect that we created above and using molecular dynamics simulations to see how gas molecules might diffuse through the membrane.
If we look at the [Solvent Accessible](surfaces-dialog) surface of our graphene, colored by the electrostatic potential, we can see that a hydrogen molecule would just barely fit through the opening, exactly as they showed!

::::{tab-set}

:::{tab-item} Solvent Accessible Surface
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_solvent_accessible_light.png
:alt: The Solvent-Accessible surface of the graphene nanopore created above.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_solvent_accessible_dark.png
:alt: The Solvent-Accessible surface of the graphene nanopore created above.
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} With a Hydrogen Molecule
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_solvent_accessible_hydrogen_light.png
:alt: The Solvent-Accessible surface of the graphene nanopore with a hydrogen molecule placed in the pore.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/building-materials/supercell/graphene_example/graphite_882_supercell_solvent_accessible_hydrogen_dark.png
:alt: The Solvent-Accessible surface of the graphene nanopore with a hydrogen molecule placed in the pore.
:align: center
:height: 300px
:class: only-dark
```
:::

::::



## See Also

- {ref}`building-materials-crystal-slab` – Create crystal surface slabs for specific Miller planes
- {ref}`building-materials-crystal-symmetry` – Perceive space groups from crystal coordinates
- {ref}`building-materials-polymer-unit-cell` – Build polymer unit cells for periodic calculations
