(tutorials-building-metal-complexes)=

# Building Metal Complexes

This tutorial demonstrates how to efficiently build coordination compounds and organometallic complexes using the [Template Tool](tools-template-tool). We'll progress from a simple complex to more sophisticated structures.

The [Template Tool](tools-template-tool) streamlines construction of metal complexes by providing pre-defined coordination geometries (octahedral, tetrahedral, square planar, etc.), a library of common ligands, and keyboard shortcuts for rapid building.

Activate the [Template Tool](tools-template-tool) with <kbd>Ctrl</kbd>+<kbd>3</kbd> or by clicking its icon in the toolbar.

## Part 1: A Simple Octahedral Complex

We'll start by building [Co(NH₃)₆]³⁺, a classic Werner complex.

**Set up the metal center**

In the **{ref}`Centers tab<template-tool-centers-tab>`**, you can either use the options panel or some {ref}`keyboard shortcuts<template-shortcuts-centers>`:
- Type `Co` to select cobalt, or pick it from the popup menu
- Press <kbd>+</kbd> three times to set the formal charge to +3
- Press <kbd>6</kbd> to select octahedral geometry

Click in empty space to place the cobalt center. Six hydrogen atoms will appear at the coordination sites.

![cobalt complex](../../_static/cobalt-complex.png){height=300px align=center}

**Add ammine ligands**

Switch to the **{ref}`Ligands tab<template-tool-ligands-tab>`** by pressing <kbd>→</kbd> or <kbd>]</kbd> or clicking the tab:
- Type `n` to select ammine (NH₃)

Click on each of the six hydrogens. Each click replaces a hydrogen with an ammine ligand.

![hexaamminecobalt complex](../../_static/cobalt-hexaammine.png){height=300px align=center}

Other ligands can also be selected by {ref}`keyboard shortcuts<template-shortcuts-ligands>`.

You now have a complete hexaamminecobalt(III) complex with idealized octahedral geometry.

:::{tip}
For other simple complexes, change the element and ligand:
- **[Fe(CN)₆]⁴⁻**: Use `Fe` and type `cn` for cyano
- **[Ni(CO)₄]**: Use `Ni`, tetrahedral (<kbd>4</kbd>), and type `co` for carbonyl
:::

## Part 2: Mixed-Ligand Complex with Different Geometries

Now we'll build [Ni(en)(NH₃)₂]²⁺, which combines a bidentate ethylenediamine with two monodentate ammine ligands. We'll also explore how the same ligand set can adopt different geometries.

### Building the Square Planar Isomer

**Create a square planar nickel center**

In the **Centers** tab:
- Type `Ni` to select nickel
- Press <kbd>+</kbd><kbd>+</kbd> for +2 charge
- Press <kbd>4</kbd><kbd>4</kbd> for square planar geometry

Click to place the center.

![Ni square planar complex](../../_static/ni-square-planar.png){height=300px align=center}


**Add ethylenediamine**

In the **Ligands** tab, type `en` to select ethylenediamine. Click on two **adjacent** hydrogen atoms (cis positions). The bidentate ligand bridges both sites, forming a five-membered chelate ring.

![Ni square planar complex](../../_static/ni-square-planar2.png){height=300px align=center}

**Add two ammine ligands**

Type `n` for ammine, then click on each of the two remaining hydrogens.

![Ni square planar complex](../../_static/ni-square-planar3.png){height=300px align=center}

### Building the Tetrahedral Isomer

Start fresh (**File → New**) and repeat with one change:
- Press <kbd>4</kbd> (not <kbd>4</kbd><kbd>4</kbd>) for tetrahedral geometry

Add the same ligands: ethylenediamine (`en`) to two adjacent hydrogens, then ammine (`n`) to the remaining two.

![Ni tetrahedral complex](../../_static/ni-tetrahedral.png){height=300px align=center}

:::{note}
Square planar and tetrahedral geometries are both common for d⁸ metals like Ni(II), Pd(II), and Pt(II). The preferred geometry depends on ligand field strength and steric factors. You can run quantum chemical calculations to compare the relative energies of the isomers.
:::

## Part 3: Organometallic Catalysts with Haptic Ligands

Finally, we'll build a Ziegler-Natta type catalyst precursor: zirconocene dichloride (Cp₂ZrCl₂). This demonstrates haptic ligand attachment and mixed ligand types.

Zirconocene dichloride has a zirconium(IV) center with two η⁵-cyclopentadienyl (Cp) rings and two chloride ligands. The Cp rings bond through all five carbon atoms (haptic bonding), creating a bent metallocene structure.

**Create the zirconium center**

We need a 4-coordinate geometry, treating each Cp as occupying one site:
- Type `Zr` to select zirconium
- Press <kbd>+</kbd> four times for +4 formal charge
- Press <kbd>4</kbd> for tetrahedral geometry

Place the center.

![Zr tetrahedral complex](../../_static/zr-tetrahedral.png){height=300px align=center}

**Add the cyclopentadienyl rings**

In the **Ligands** tab, type `cp` (or `e5`) to select η⁵-cyclopentadienyl.

Click on one hydrogen. The entire Cp ring attaches, with all five carbons oriented toward the metal. Click on an adjacent hydrogen to add the second Cp ring.

![(Cp)2 Zr complex](../../_static/cp2-zr.png){height=300px align=center}

**Add the chloride ligands**

The [Template Tool](tools-template-tool)'s ligand library focuses on organic ligands. For chlorides, switch to the [Draw Tool](tools-draw-tool) (<kbd>Ctrl</kbd>+<kbd>2</kbd>), select chlorine from the element selector, and click on each remaining hydrogen to replace it with Cl.

![(Cp)2 ZrCl2 complex](../../_static/cp2-zr-cl2.png){height=300px align=center}

You could also type `e2` to select η²-ethylene to insert in one site.

![Ziegler-Natta complex](../../_static/cp2-zr-ethylene.png){height=300px align=center}

:::{tip}
Try building related catalysts:
- **Titanocene dichloride**: Use `Ti` instead of `Zr`
- **Half-sandwich complexes**: Use only one Cp ring with other ligands
- **η⁶-arene complexes**: Use `e6` for benzene coordination
:::

The ligand library also has other haptic coordination modes, such as a distorted η³-cyclopentadienyl for fluxional behavior.

## Summary

| Complex Type | Key Steps |
|--------------|-----------|
| Simple octahedral | Element → charge → <kbd>6</kbd> → place → add 6 monodentate ligands |
| Mixed-ligand | Element → charge → geometry → bidentate first → fill remaining sites |
| Geometry comparison | <kbd>4</kbd> for tetrahedral, <kbd>44</kbd> for square planar |
| Haptic complexes | Use `cp`, `e5`, `e6` → each haptic ligand counts as one site |

## See Also

- [Template Tool Reference](tools-template-tool) for the complete list of keyboard shortcuts and options
- [Template Tool: Creating New Ligands](tools-template-tool) for building custom ligands
