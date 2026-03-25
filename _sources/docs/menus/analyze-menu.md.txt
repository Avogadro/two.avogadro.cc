(menus-analyze-menu)=

# Analyze Menu

The Analyze menu contains a wide array of analysis tools for analyzing molecular properties, orbital surfaces, vibrational modes, conformer data, and plotting spectra, as well as tools for performing QTAIM analysis.

Properties
: See [Properties](properties-dropdown).

Create Surfaces
: See [Surfaces Dialog](surfaces-dialog).

Molecule Orbitals
: Open the molecular orbital window (requires orbitals from a quantum chemistry program).

:::{dropdown} Molecular Orbital Window
:color: info
:icon: image

```{image} /_static/menus/analyze-menu/molecular_orbital_window.png
:alt: Example of the molecular orbital window
:align: center
:width: 360px
:class: dark-light
```
:::

QTAIM
: Run Quantum Theory of Atoms In Molecules (QTAIM) analyses (requires a `.wfn` file).

Vibrational Modes
: Open a window with vibrational modes from a quantum chemistry program.

Plot Conformer Data
: Create plots of the conformers in the current document.

Plot Spectra
: Plot electronic and vibrational spectra (IR, NMR, etc.)


(properties-dropdown)=
## Properties

Molecular
: Open a dialog containing basic molecular properties as well as any additional information from a quantum chemical output.

:::{dropdown} Molecular Properties Dialog
:color: info
:icon: image

```{image} /_static/menus/analyze-menu/molecular_properties_dialog.png
:alt: Example of the molecular properties dialog
:align: center
:width: 43%
:class: dark-light
```
:::

Atom Properties
: Open a dialog containing atomic coordinate information as well as any additional information from a quantum chemical output.

:::{dropdown} Atom Properties Dialog
:color: info
:icon: image

```{image} /_static/menus/analyze-menu/atom_properties_dialog.png
:alt: Example of the atom properties dialog
:align: center
:class: dark-light
```
:::

Bond Properties
: Open a dialog containing bonding information.

:::{dropdown} Bond Properties Dialog
:color: info
:icon: image

```{image} /_static/menus/analyze-menu/bond_properties_dialog.png
:alt: Example of the Bond Properties Dialog
:align: center
:width: 67%
:class: dark-light
```
:::

Angle Properties
: Open a dialog containing information about the angles formed by atoms.

:::{dropdown} Angle Properties Dialog
:color: info
:icon: image

```{image} /_static/menus/analyze-menu/angle_properties_dialog.png
:alt: Example of the Angle Properties Dialog
:align: center
:width: 49%
:class: dark-light
```
:::

Torsion Properties
: Open a dialog containing information about the dihedrals formed by atoms.

:::{dropdown} Torsion Properties
:color: info
:icon: image

```{image} /_static/menus/analyze-menu/torsion_properties_dialog.png
:alt: Example of the Torsion Properties Dialog
:align: center
:width: 59%
:class: dark-light
```
:::

Residue Properties
: Open a dialog containing information about any amino acid residues.

:::{dropdown} Residue Properties
:color: info
:icon: image

```{image} /_static/menus/analyze-menu/residue_properties_dialog.png
:alt: Example of the Residue Properties Dialog
:align: center
:width: 74%
:class: dark-light
```
:::

Conformer Properties
: Open a dialog containing information about any conformers present in the document.

:::{dropdown} Conformer Properties Dialog
:color: info
:icon: image

```{image} /_static/menus/analyze-menu/conformer_properties_dialog.png
:alt: Example of the Conformer Properties Dialog
:align: center
:width: 36%
:class: dark-light
```
:::

Symmetry
: Open the symmetry dialog, where you can access information about the molecule's point group, visualize symmetry operations, and identify symmetry-equivalent atoms.

:::{dropdown} Symmetry Dialog
:color: info
:icon: image

```{image} /_static/menus/analyze-menu/symmetry_dialog.png
:alt: Example of the Symmetry Dialog
:align: center
:width: 48%
:class: dark-light
```
:::

(surfaces-dialog)=
## Surfaces Dialog

The surfaces dialog has several useful tools for calculating and rendering various types of surfaces.

```{figure} /_static/menus/analyze-menu/surfaces_dialog.png
:alt: Example of the surfaces dialog
:align: center
:width: 420px
:class: dark-light
```

### Surface Types and Coloring

You can choose to render several surfaces from the first dropdown, including a Van der Waals surface, solvent accessible and solvent excluded surfaces, molecular orbitals, and electron density. The latter two require an output from a quantum calculation.

For any surface other than a molecular orbital, you can choose to color the surface by the electrostatic potential, and select from several color maps.

```{figure} /_static/menus/analyze-menu/coronene_colored_density_dark.png
:alt: Example of the electron density of coronene colored by the electrostatic potential
:align: center
:class: only-dark
:height: 300px
```
```{figure} /_static/menus/analyze-menu/coronene_colored_density_light.png
:alt: Example of the electron density of coronene colored by the electrostatic potential
:align: center
:class: only-light
:height: 300px
```

:::{dropdown} Available Color Maps
:color: info
:icon: image

```{image} /_static/avogadro_charge_colors.svg
:alt: The color maps available for coloring by electrostatic potential
:align: center
:class: only-light
```
```{image} /_static/avogadro_charge_colors_darkmode.svg
:alt: The color maps available for coloring by electrostatic potential
:align: center
:class: only-dark
```
:::

### Resolution

The resolution option sets the spacing between volume elements in the rendered image.

::::{tab-set}

:::{tab-item} Very Low
```{image} /_static/menus/analyze-menu/pyrazine_homo_verylow_res_light.png
:alt: The HOMO of Pyrazine with the Very Low resolution setting.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_homo_verylow_res_dark.png
:alt: The HOMO of Pyrazine with the Very Low resolution setting.
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} Low
```{image} /_static/menus/analyze-menu/pyrazine_homo_low_res_light.png
:alt: The HOMO of Pyrazine with the Low resolution setting.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_homo_low_res_dark.png
:alt: The HOMO of Pyrazine with the Low resolution setting.
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} Medium
:selected:
```{image} /_static/menus/analyze-menu/pyrazine_homo_medium_res_light.png
:alt: The HOMO of Pyrazine with the Medium resolution setting.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_homo_medium_res_dark.png
:alt: The HOMO of Pyrazine with the Medium resolution setting.
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} High
```{image} /_static/menus/analyze-menu/pyrazine_homo_high_res_light.png
:alt: The HOMO of Pyrazine with the High resolution setting.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_homo_high_res_dark.png
:alt: The HOMO of Pyrazine with the High resolution setting.
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} Very High
```{image} /_static/menus/analyze-menu/pyrazine_homo_veryhigh_res_light.png
:alt: The HOMO of Pyrazine with the Very High resolution setting.
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_homo_veryhigh_res_dark.png
:alt: The HOMO of Pyrazine with the Very High resolution setting.
:align: center
:height: 300px
:class: only-dark
```
:::

::::

:::{hint}
While a higher resolution may be desirable, keep in mind that the time to compute the surface scales cubically!
:::

### Isosurface Value

The Isosurface value determines the cutoff distance for the surface by dictating the lowest value of the volume scalars to display. There is not an accepted set of isosurface values that should be used in papers, however it is recommended to stick to 0.01–0.10, and it is strongly encouraged to report your isosurface values if you include a surface in a figure. 

The reason for this becomes evident with the figure below, which shows the HOMO of pyrazine at 10 different isosurface values. As you move through the different values, you'll see that the orbital overlap between atoms can change drastically as a function of the chosen isosurface value. At 0.01, you might be tempted to say the nitrogens on opposite ends of the pyrazine have bonding character right through the middle of the molecule, but as we know, this is not the case. Only once the isosurface value reaches ~0.08 do we see that in fact the nature of the HOMO is more likely a pair of $\sigma_b$ orbitals between the carbon atoms and two lone pairs on the nitrogen atoms.

::::{tab-set}

:::{tab-item} 0.01
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.01_light.png
:alt: HOMO of pyrazine with an Isosurface value of 0.01
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.01_dark.png
:alt: HOMO of pyrazine with an Isosurface value of 0.01
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.02
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.02_light.png
:alt: HOMO of pyrazine with an Isosurface value of 0.02
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.02_dark.png
:alt: HOMO of pyrazine with an Isosurface value of 0.02
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.03 (Default)
:selected:
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.03_light.png
:alt: HOMO of pyrazine with an Isosurface value of 0.03
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.03_dark.png
:alt: HOMO of pyrazine with an Isosurface value of 0.03
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.04
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.04_light.png
:alt: HOMO of pyrazine with an Isosurface value of 0.04
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.04_dark.png
:alt: HOMO of pyrazine with an Isosurface value of 0.04
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.05
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.05_light.png
:alt: HOMO of pyrazine with an Isosurface value of 0.05
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.05_dark.png
:alt: HOMO of pyrazine with an Isosurface value of 0.05
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.06
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.06_light.png
:alt: HOMO of pyrazine with an Isosurface value of 0.06
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.06_dark.png
:alt: HOMO of pyrazine with an Isosurface value of 0.06
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.07
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.07_light.png
:alt: HOMO of pyrazine with an Isosurface value of 0.07
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.07_dark.png
:alt: HOMO of pyrazine with an Isosurface value of 0.07
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.08
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.08_light.png
:alt: HOMO of pyrazine with an Isosurface value of 0.08
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.08_dark.png
:alt: HOMO of pyrazine with an Isosurface value of 0.08
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.09
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.09_light.png
:alt: HOMO of pyrazine with an Isosurface value of 0.09
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.09_dark.png
:alt: HOMO of pyrazine with an Isosurface value of 0.09
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.10
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.10_light.png
:alt: HOMO of pyrazine with an Isosurface value of 0.10
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_iso/pyrazine_homo_iso_0.10_dark.png
:alt: HOMO of pyrazine with an Isosurface value of 0.10
:align: center
:height: 300px
:class: only-dark
```
:::

::::

It should be noted, however, that while one may initially conclude that all orbitals should be shown with an isosurface value of ~0.08, this is not the case. The isosurface value is not universal across varying system sizes, which can be seen simply by examining the HOMO of coronene below. At 0.08 there is essentially zero bonding character shown at all, when we know that the HOMO of coronene should be a $\pi$-bonding network. It could be suggested that the correct isosurface value in this case is between 0.03 and 0.04, which both show the bonding nature of the HOMO quite well.

::::{tab-set}

:::{tab-item} 0.01
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.01_light.png
:alt: HOMO of coronene with an Isosurface value of 0.01
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.01_dark.png
:alt: HOMO of coronene with an Isosurface value of 0.01
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.02
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.02_light.png
:alt: HOMO of coronene with an Isosurface value of 0.02
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.02_dark.png
:alt: HOMO of coronene with an Isosurface value of 0.02
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.03 (Default)
:selected:
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.03_light.png
:alt: HOMO of coronene with an Isosurface value of 0.03
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.03_dark.png
:alt: HOMO of coronene with an Isosurface value of 0.03
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.04
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.04_light.png
:alt: HOMO of coronene with an Isosurface value of 0.04
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.04_dark.png
:alt: HOMO of coronene with an Isosurface value of 0.04
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.05
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.05_light.png
:alt: HOMO of coronene with an Isosurface value of 0.05
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.05_dark.png
:alt: HOMO of coronene with an Isosurface value of 0.05
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.06
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.06_light.png
:alt: HOMO of coronene with an Isosurface value of 0.06
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.06_dark.png
:alt: HOMO of coronene with an Isosurface value of 0.06
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.07
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.07_light.png
:alt: HOMO of coronene with an Isosurface value of 0.07
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.07_dark.png
:alt: HOMO of coronene with an Isosurface value of 0.07
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.08
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.08_light.png
:alt: HOMO of coronene with an Isosurface value of 0.08
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.08_dark.png
:alt: HOMO of coronene with an Isosurface value of 0.08
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.09
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.09_light.png
:alt: HOMO of coronene with an Isosurface value of 0.09
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.09_dark.png
:alt: HOMO of coronene with an Isosurface value of 0.09
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} 0.10
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.10_light.png
:alt: HOMO of coronene with an Isosurface value of 0.10
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/coronene_iso/coronene_homo_iso_0.10_dark.png
:alt: HOMO of coronene with an Isosurface value of 0.10
:align: center
:height: 300px
:class: only-dark
```
:::

::::

In summary, always ensure that you have chosen a suitable isosurface value for publications, and more importantly, **always report isosurface values**.

### Smoothing

The smoothing option, as the name implies, affects how visually smooth the surface is. In general, this has a more pronounced effect on the Van der Waals and Solvent Accessible/Excluded surfaces. Unlike the resolution, the smoothing value has a significantly smaller effect on compute time.

::::{tab-set}

:::{tab-item} Light (1)
```{image} /_static/menus/analyze-menu/pyrazine_vdw_light_smoothing_light.png
:alt: Van der Waals surface of pyrazine with Light (Level 1) smoothing
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_vdw_light_smoothing_dark.png
:alt: Van der Waals surface of pyrazine with Light (Level 1) smoothing
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} Level 3
```{image} /_static/menus/analyze-menu/pyrazine_vdw_3_smoothing_light.png
:alt: Van der Waals surface of pyrazine with Level 3 smoothing
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_vdw_3_smoothing_dark.png
:alt: Van der Waals surface of pyrazine with Level 3 smoothing
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} Medium (5)
:selected:
```{image} /_static/menus/analyze-menu/pyrazine_vdw_medium_smoothing_light.png
:alt: Van der Waals surface of pyrazine with Medium (Level 5) smoothing
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_vdw_medium_smoothing_dark.png
:alt: Van der Waals surface of pyrazine with Medium (Level 5) smoothing
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} Level 7
```{image} /_static/menus/analyze-menu/pyrazine_vdw_7_smoothing_light.png
:alt: Van der Waals surface of pyrazine with Level 7 smoothing
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_vdw_7_smoothing_dark.png
:alt: Van der Waals surface of pyrazine with Level 7 smoothing
:align: center
:height: 300px
:class: only-dark
```
:::

:::{tab-item} Strong (9)
```{image} /_static/menus/analyze-menu/pyrazine_vdw_strong_smoothing_light.png
:alt: Van der Waals surface of pyrazine with Strong (Level 9) smoothing
:align: center
:height: 300px
:class: only-light
```
```{image} /_static/menus/analyze-menu/pyrazine_vdw_strong_smoothing_dark.png
:alt: Van der Waals surface of pyrazine with Strong (Level 9) smoothing
:align: center
:height: 300px
:class: only-dark
```
:::

::::
