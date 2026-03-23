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
:open:

```{image} ../../_static/molecular_orbital_dialog.png
:alt: Example of the molecular orbital window
:align: center
:width: 250px
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
:open:
```{image} ../../_static/molecular_properties_dialog.png
:alt: Example of the molecular properties dialog
:align: center
:width: 360px
:class: dark-light
```
:::

Atom Properties
: Open a dialog containing atomic coordinate information as well as any additional information from a quantum chemical output.

:::{dropdown} Atom Properties Dialog
:color: info
:icon: image
:open:

```{image} ../../_static/atom_properties_dialog.png
:alt: Example of the atom properties dialog
:align: center
:class: dark-light
```
:::

Bond Properties
: Open a dialog containing bonding information.

:::{dropdown} Bond Properties
:color: info
:icon: image
:open:

```{image} ../../_static/bond_properties_dialog.png
:alt: Example of the Bond Properties Dialog
:align: center
:class: dark-light
```
:::

Angle Properties
: Open a dialog containing information about the angles formed by atoms.

:::{dropdown} Example Dialog
:color: info
:icon: image
:open:

```{image} ../../_static/angle_properties_dialog.png
:alt: Example of the Angle Properties Dialog
:align: center
:width: 360px
:class: dark-light
```
:::

Torsion Properties
: Open a dialog containing information about the dihedrals formed by atoms.

:::{dropdown} Torsion Properties
:color: info
:icon: image
:open:

```{image} ../../_static/torsion_properties_dialog.png
:alt: Example of the Torsion Properties Dialog
:align: center
:width: 250px
:class: dark-light
```
:::

Residue Properties
: @ghutchis

Conformer Properties
: Open a dialog containing information about any conformers present in the document.

:::{dropdown} Example Dialog
:color: info
:icon: image
:open:

```{image} ../../_static/conformer_properties_dialog.png
:alt: Example of the Conformer Properties Dialog
:align: center
:width: 250px
:class: dark-light
```
:::

Symmetry
: Open the symmetry dialog, where you can access information about the molecule's point group, visualize symmetry operations, and identify symmetry-equivalent atoms.

(surfaces-dialog)=
## Surfaces Dialog

The surfaces dialog has several useful tools for calculating and rendering various types of surfaces.

:::{dropdown} Example Surfaces Dialog
:color: info
:icon: image
:open:
```{image} ../../_static/surfaces_dialog.png
:alt: Example of the surfaces dialog
:align: center
:width: 420px
:class: dark-light
```
:::

### Surface Types and Coloring

You can choose to render several surfaces from the first dropdown, including a Van der Waals surface, solvent accessible and solvent excluded surfaces, molecular orbitals, and electron density. The latter two require an output from a quantum calculation.

For any surface other than a molecular orbital, you can choose to color the surface by the electrostatic potential, and select from several color maps.

::::{dropdown} Electron Density colored by Electrostatic Potential
:color: info
:icon: image
:open:

```{image} ../../_static/example_electron_density.png
:alt: Example of the electron density of coronene colored by the electrostatic potential
:align: center
:class: dark-light
```

:::{dropdown} Available Color Maps
:color: info
:icon: image

```{image} ../../_static/avogadro_charge_colors.svg
:alt: The color maps available for coloring by electrostatic potential
:align: center
:class: only-light
```
```{image} ../../_static/avogadro_charge_colors_darkmode.svg
:alt: The color maps available for coloring by electrostatic potential
:align: center
:class: only-dark
```
:::
::::

### Resolution

The resolution option sets the spacing between volume elements in the rendered image.

::::{tab-set}

:::{tab-item} Very Low
```{image} ../../_static/pyrazine_homo_verylow_res.png
:alt: The HOMO of Pyrazine with the Very Low resolution setting.
:align: center
:class: dark-light
```
:::

:::{tab-item} Low
```{image} ../../_static/pyrazine_homo_low_res.png
:alt: The HOMO of Pyrazine with the Low resolution setting.
:align: center
:class: dark-light
```
:::

:::{tab-item} Medium
:selected:
```{image} ../../_static/pyrazine_homo_medium_res.png
:alt: The HOMO of Pyrazine with the Medium resolution setting.
:align: center
:class: dark-light
```
:::

:::{tab-item} High
```{image} ../../_static/pyrazine_homo_high_res.png
:alt: The HOMO of Pyrazine with the High resolution setting.
:align: center
:class: dark-light
```
:::

:::{tab-item} Very High
```{image} ../../_static/pyrazine_homo_veryhigh_res.png
:alt: The HOMO of Pyrazine with the Very High resolution setting.
:align: center
:class: dark-light
```
:::

::::

:::{hint}
While a higher volume may be desirable, keep in mind that the time to compute the surface scales cubically!
:::

### Isosurface Value

The Isosurface value determines the cutoff distance for the surface by dictating the lowest value of the volume scalars to display. There is not an accepted set of isosurface values that should be used in papers, however it is recommended to stick to 0.01-0.10, and it is strongly encouraged to report your isosurface values if you include a surface in a figure.

### Smoothing

The smoothing option, as the name implies, affects how visually smooth the surface is. In general, this has a more pronounced effect on the Van der Waals and Solvent Accessible/Excluded surfaces. Unlike the resolution, the smoothing value has a significantly smaller effect on compute time.

::::{tab-set}

:::{tab-item} Light
```{image} ../../_static/pyrazine_van_der_waals_light_smoothing.png
:alt: Van der Waals surface of pyrazine with light smoothing
:align: center
:class: dark-light
```
:::

:::{tab-item} Medium
:selected:
```{image} ../../_static/pyrazine_van_der_waals_medium_smoothing.png
:alt: Van der Waals surface of pyrazine with Medium smoothing
:align: center
:class: dark-light
```
:::

:::{tab-item} Strong
```{image} ../../_static/pyrazine_van_der_waals_strong_smoothing.png
:alt: Van der Waals surface of pyrazine with Strong smoothing
:align: center
:class: dark-light
```
:::

::::
