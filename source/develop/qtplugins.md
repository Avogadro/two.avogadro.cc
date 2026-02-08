(develop-qtplugins)=

# Avogadro::QtPlugins

There are a wide variety of plugins in separate directories, providing
tools, render types, and commands. Some may provide more than one of these
for full functionality (e.g., symmetry perception includes both a command and a render type).

What follows is a list of core plugins and brief descriptions. A few plugins are listed in multiple places:

## Tools

- **aligntool** - align molecule to a frame of reference
- **bondcentrictool** - bond centric manipulation (length, angle, dihedral)
- **editor** - freehand drawing of atoms and bonds
- **label** - edit atom labels (also a render type)
- **manipulator** - move and rotate atoms and selections
- **measuretool** - measure bond lengths, angles, and dihedrals
- **navigator** - move the camera view
- **playertool** - play animations / trajectories
- **selectiontool** - select atoms individually or in a rectangle
- **templatetool** - insert ligands, functional groups, and metal geometries

## Render Types

- **ballandstick** - the default ball-and-stick render type
- **cartoons** - protein backbone and cartoon renderings
- **closecontacts** - close contacts between atoms
- **dipole** - dipole moment
- **force** - forces on atoms (from vibrations or molecular dynamics)
- **label** - atom and other labels - also a tool
- **licorice** - stick or licorice rendering
- **noncovalent** - hydrogen, chalcogen bonds and other non-covalent interactions
- **overlayaxes** - reference axes
- **qtaim** - QTAIM rendering (critical points, etc.), also a command
- **surfacerender** - surfaces, orbitals, volumetric etc.
- **symmetry** - rendering of symmetry elements, also a command
- **vanderwaals** - van der Waals spheres
- **wireframe** - wireframe line rendering

## Main Commands

- **applycolors** - Apply colors to atoms (e.g., by partial charge, etc.)
- **bonding** - Assign bonds and bond orders, break bonds
- **coordinateeditor** - Edit, copy and paste atoms and 3D coordinates
- **copypaste** - Cut, copy and paste commands
- **crystal** - Commands for handling basic crystal structure properties
- **focus** - Focus and unfocus the view on a selection
- **forcefield** - Optimize and run force field calculations, including via scripts
- **hydrogens** - Add, remove, and adjust hydrogen atoms
- **insertdna** - Insert DNA fragments
- **insertfragment** - Insert molecules
- **lineformatinput** - Insert from SMILES or InChI line formats
- **molecularproperties** - Molecular property dialogs
- **openbabel** - Open Babel commands, including file formats, force fields, charges, etc.
- **propertytables** - Atom, bond, angle, and torsion property spreadsheets
- **select** - Selection commands
- **spacegroup** - Handle filling and standardizing the unit cell based on space groups
- **surfaces** - Generate molecular surfaces and orbitals
- **symmetry** - Perceive molecular symmetry and symmetrize coordinates
- **vibrations** - Animate vibrations

## Script Commands

- **commandscripts** - Add menu commands from Python scripts
- **configurepython** - Configure the Python environment to use for scripts
- **forcefield** - Optimize and run force field calculations, including via scripts
- **plugindownloader** - Download and install Python scripts
- **quantuminput** - Use Python scripts for many quantum chemical input generators (e.g., Orca, Gaussian, Q-Chem, etc.)
- **scriptcharges** - Assign atomic partial charges using Python scripts (e.g., from `xtb` or `antechamber`)
- **scriptfileformats** - Import various file formats using Python scripts

## Input Generator Commands

- **apbs** - Input for the APBS program
- **cp2kinput** - Input for CP2K
- **gamessinput** - Input for GAMESS-US
- **lammpsinput** - Input for LAMMPS
- **openmminput** - Input for OpenMM simulations
- **quantuminput** - Use Python scripts for many quantum chemical input generators (e.g., Orca, Gaussian, Q-Chem, etc.)

## Import Commands

- **fetchpdb** - Fetch molecules from the Protein Data Bank (PDB)
- **importpqr** - Import molecules from the Pitt Quantum Repository
- **networkdatabases** - Fetch molecules by name from the NIH Chemical Resolver

## Export Commands

- **3dmol** - Export the current view for 3dmol.js rendering in a webpage
- **ply** - Export a 3D PLY format file of the current view
- **povray** - Export a POV-Ray scene of the current view
- **svg** - Export a SVG render of the current image
- **vrml** - Export a VRML / WRL file of the current view

## Plotting Commands

- **spectra** - plot vibrational (IR, Raman), electronic (UV), NMR and other computed spectra
- **plotpdf** - plot the probability distribution function (PDF)
- **plotrmsd** - plot RMSD across multiple coordinate sets (e.g., in an MD trajectory)
- **plotxrd** - plot simulated x-ray diffraction patterns from a crystal structure

## Miscellaneous

- **centroid**
- **customelements**
- **resetview**
- **yaehmop**
