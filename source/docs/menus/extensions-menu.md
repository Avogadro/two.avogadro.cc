(menus-extensions-menu)=

# Extensions Menu

The Extensions menu contains commands for plugins and built-in functions.

Optimize Geometry {kbd}`Ctrl+Alt+O`
: Optimize the geometry of the current molecule(s) using a Molecular Mechanics Force Field.

Calculate
: See [Calculate](calculate_dropdown).

Download Plugins...
: See [Plugin Interface](plugin_interface).

Python Settings...
: Open a dialog to modify the Python path that Avogadro 2 uses.

User Interface Language...
: Open a dialog to switch the language in Avogadro 2.

Yaehmop
: Open a submenu that contains features from Yaehmop.

Edit Color Opacity Map...
: TODO

Periodic Table
: Open an interactive periodic table dialog.

:::{note}
The colorations of each element's box correspond to the color of each element when drawn.
:::

Open Babel
: See [Open Babel Interface](open_babel_interface)

(calculate_dropdown)=
#### Calculate

The Calculate dropdown contains several functions that calculate properties of the current molecule(s), such as:

Energy
: Calculate the energy of the molecule using the currently selected Force Field.

Forces
: Calculate the forces in the molecule using the currently selected Force Field.

Configure...
: Open the Geometry Optimization configuration dialog. See [Configure Dialog](configure_dialog)

Freeze Selected Atoms
: Freeze any selected atoms, such that they do not move when using the Optimize Geometry function.

Unfreeze Selected Atoms
: Unfreezes any selected atoms, allowing them to move when using the Optimize Geometry function.

(configure_dialog)=
##### Configure...

The Configure dialog allows the user to modify some of the parameters relevant to the Force Field optimization, such as the specific Force Field used, the convergence criteria, and the step limit.

Force Field
: Select the Force Field that will be used in the Optimize Geometry function.

:::{note}
The selection dropdown is unavailable when the Autodetect box is checked.
:::

:::{note}
The generally available Force Fields are MMFF94, GAFF, UFF, and LJ. Of these Force Fields, MMFF94 and GAFF are unavailable for charged molecules and
:::