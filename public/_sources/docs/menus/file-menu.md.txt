(menus-file-menu)=

# File Menu

The File menu contains commands useful for opening, importing, and exporting molecules.

New {kbd}`Ctrl+N`
: Create a new molecule document.

Open {kbd}`Ctrl+O`
: Open a file containing molecule information from a file browser.

Open Recent
: Display a list of the 10 most recent files opened.

Close {kbd}`Ctrl+W`
: Close the current window.

Save {kbd}`Ctrl+S`
: Save the current molecule.

Save As... {kbd}`Ctrl+Shift+S`
: Save the current molecule as a CJSON (`.cjson`) or CML (`.cml`) file.

Import
: See [Import](import_menu)

Export
: See [Export](export_menu)

Quit {kbd}`Ctrl+Q`
: Close Avogadro 2

(import_menu)=
#### Import Menu

The Import menu contains commands useful for importing molecules to the current document, such as downloading a molecule by name, fetching it from the Protein Data Bank (PDB), or importing a crystal structure.

Download by Name
: Load a molecule by its common name.

:::{note}
This is most likely to work for common molecules such as caffeine, and is not guaranteed to work for every molecule name.
:::

Fetch from PDB
: Download a PDB entry by its identifier.

Crystal
: Import a crystal structure from those provided by Avogadro.

(export_menu)=
#### Export Menu

Export the current molecule as chemical file format or as a graphic.

Molecule
: Open a file dialog to select a format to save the current molecule to.

Graphics
: Open a file dialog to save the current screen as a PNG.

3DMol HTML Snippet
: Automatically generate HTML to render the molecule in a web browser.

SVG
: Export a **2D** rendering of the current molecule as a scalable vector graphic (SVG).

PLY Render
: Export a 3D render of the current molecule in a format readable by CAD software such as [Blender](https://www.blender.org/).

POV-Ray Render
: Export a 3D render of the current molecule in a format readable by [POV-Ray](https://www.povray.org/documentation/view/3.60/802/).

VRML Render
: Export a 3D render of the current molecule in a format readable by CAD software.
