(menus-view-menu)=

# View Menu

The View menu contains several features useful for rotating the camera, coloring atoms, and choosing rendering settings.

Center
: Center the camera around the origin and align your view to the axes

Align View to Axes
: Align your view to the axes, but do not move the camera.

Focus Selection
: Focus the camera on the selected atoms. This will cause any rotations to be centered around the focused atoms.

Unfocus
: Undo the camera focusing.

Rendering
: Open a dialog to select the rendering options.

Set Background Color
: Open a dialog to change the background color.

Projection
: Select between perspective and orthographic projections.

:::{note}
An orthographic projection means all atoms are the same size, while a perspective projection means that atoms that are closer to the camera will be larger.
:::

Color Atoms
: Change the color of the atoms by a property with one of the available colormaps, or by a custom color. By default, this colors atoms by their element. There are two sets of available colormaps for atoms, one set for charge that works on a blue-red motif, and another for color-by-index and color-by-distance that has a larger range of colors.

:::{dropdown} Show Available Colormaps
:color: info
:icon: image

```{image} ../../_static/avogadro_charge_colors.svg
:alt: Colormaps available when coloring by charge.
:align: center
:class: only-light
```
```{image} ../../_static/avogadro_charge_colors_darkmode.svg
:alt: Colormaps available when coloring by charge.
:align: center
:class: only-dark
```

```{image} ../../_static/avogadro_colors.svg
:alt: Colormaps available when coloring by index or by distance
:align: center
:class: only-light
```
```{image} ../../_static/avogadro_colors_darkmode.svg
:alt: Colormaps available when coloring by index or by distance
:align: center
:class: only-dark
```

:::

Color Residues
: Color protein structures by various properties.

:::{note}
To see these colors you must have the `Cartoons` display type enabled.
:::
