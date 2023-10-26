# Major New Features

### Speed and Stability

A major concern with Avogadro 1.x was speed on larger systems including biomolecules (protein, DNA/RNA) and materials. Even viewing / rotating large molecules would be slow, much less editing or performing optimizations or dynamics calculations.

We also know that Avogadro 1.x crashed for multiple reasons - not least because we used older rendering code which was not well supported by modern graphics cards and drivers.

Avogadro 2.0 has been rewritten from the ground up. **Avogadro v2 was designed for fast modern rendering and improved stability. It is a platform to make it easy to build the next generation of molecular and materials visualization and editing tools.**

### Rendering

Avogadro's new rendering framework _**easily**_ handles tens and hundreds of thousands of atoms – not just because hardware has improved but by using new 3D graphics rendering methods which make better use of modern GPUs.

<figure><img src="../.gitbook/assets/Covid Spike (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/6vxx-yes.png" alt="Example of real-time shadows and ambient occlusion on the COVID spike protein (6vxx)"><figcaption><p>Example of real-time shadows and depth effects on COVID spike protein (PDB: 6vxx) - around 25,000 atoms</p></figcaption></figure>

#### New real-time shadows and depth effects

The new rendering system not only handles more atoms, but real-time shadows (also called ambient occlusion) provide depth effects which make even smaller molecules look more like physical models.

<figure><img src="../.gitbook/assets/Caffeine.png" alt="Ball and stick model of caffeine molecule illustrating real-time shading" width="222"><figcaption><p>Ball and stick model of caffeine molecule showing real-time shading</p></figcaption></figure>

#### New "close contact" rendering

This new rendering type will show various types of non-bonded close-contact interactions, including salt bridge and repulsive electrostatic interactions.

<figure><img src="../.gitbook/assets/CloseContact.png" alt="Foldamer molecule highlighting non-bonded close contacts (at 2.2 A separation) in dashed grey lines" width="375"><figcaption><p>Close contact interactions as grey dashed lines</p></figcaption></figure>

#### New non-bonded rendering analysis, including hydrogen bonds, halogen bonds, and chalcogen bonds

Another new rendering type highlights hydrogen bonds, halogen and chalcogen non-bonded interactions.

<figure><img src="../.gitbook/assets/DNA-hbonds.png" alt="DNA bases highlighting hydrogen bonds" width="375"><figcaption><p>DNA bases highlighting hydrogen bonding interactions</p></figcaption></figure>

#### New cartoon / ribbon styles for proteins

<figure><img src="../.gitbook/assets/covid-spike.png" alt="Example of new protein cartoon ribbons in the COVID spike protein 6vxx"><figcaption><p>Example ribbon / cartoon view of COVID spike protein (PDB: 6vxx)</p></figcaption></figure>

### Layers

A major new feature in Avogadro 2 is the layer system. You can create new layers for a wide variety of tasks:

* hide part of the molecule (e.g., put solvent into one layer and hide it during analysis or editing)
* change rendering options (e.g., display a protein with cartoon, but show a few key residues with ball-and-stick rendering)
* lock a layer to prevent editing (e.g., moving a molecule to bind with a locked surface or protein active site)

A new section on the Layer dock and tutorials on using layers for common tasks is available.

Future development will help use layers for complex simulations (e.g., QM/MM with one layer defining the quantum chemical fragments).

### Symmetry Properties

Avogadro 2 includes a new tool to perceive molecular symmetry, display symmetry elements, and explore subgroups and classes of symmetric atoms. You can find it under the Analysis => Properties submenu.

<figure><img src="../.gitbook/assets/Symmetry.png" alt=""><figcaption><p>Symmetric perception (<span class="math">I_h</span>) and rendering of inversion center and <span class="math">C_5</span>rotation axes in a <span class="math">C_{60}</span> molecule.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/Symmetry.png" alt="Example of symmetry detection and rendering in C60" width="375"><figcaption><p>Example of symmetry detection and rendering on C60 molecule, showing inversion center and C5 rotations</p></figcaption></figure>

### Template Tool

A new "template tool" makes it easy to build inorganic/organometallic complexes with different geometries and ligands.&#x20;

<figure><img src="../.gitbook/assets/centers.png" alt="Example of new template tool, indicating octahedral iron atom geometry" width="270"><figcaption><p>Example of template tool to insert octahedral iron fragment</p></figcaption></figure>

The "click to add" feature for ligands also works well for adding functional groups like phenyl rings, or a wide range of other fragments.

<figure><img src="../.gitbook/assets/ligands.png" alt="Example of template tool for ligands, including inserting bidentate acac ligand" width="264"><figcaption><p>Example of template tool ligand insertion, including bidentate ligands such as acac</p></figcaption></figure>

### Solvent Accessible and Solvent Excluded Surfaces



### Flexible Electrostatics Models

Since there are many ways to approximate electrostatics in molecules, including atomic partial charges, there is a new framework for assigning electrostatics. By default, Avogadro includes several partial charge models from Open Babel, including Gasteiger charges, EEM, and MMFF94 methods.

If installed and available in your command path, `xtb` (GFN2) and `antechamber` (AM1BCC) charges can be assigned using Python scripts.

The framework allows installing additional Python scripts, which could assign atomic partial charges or electrostatic potential surfaces using other programs, ML models, etc.

<figure><img src="../.gitbook/assets/EEM Charges.png" alt="" width="375"><figcaption><p>Example molecule with EEM atom colors (red = negative, blue = positive)</p></figcaption></figure>

### New Analysis Tools

Plot theoretical x-ray diffraction patterns for crystals

Plot pair distribution functions

Band structure diagrams with Yaehmop `eht_bind`

### Python Commands / Plugins

With Avogadro 2, it's easier than ever to create a quick Python script and add it as an Avogadro command. These scripts can modify the molecule / atoms (e.g., add a solvent box), run analysis (e.g., assign R and S stereochemical labels with `rdkit`), optimize the geometry, create nanoparticles or nanotubes using installed Python modules (e.g., `pymatgen` or `ASE`), generate ice crystal structures, solvate molecules, and many more.

Current plugin types include:

* input generators
* menu commands
* electrostatics models
* data (e.g., molecule and crystal fragments)

You can also share your plugins through GitHub and others can download and install or update to new versions through the "Download Extensions" command:

<figure><img src="../.gitbook/assets/Plugin Downloader.png" alt=""><figcaption><p>Download plugins interface to install new commands, input generators, etc.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/Download.png" alt="" width="563"><figcaption><p>Download Python extension scripts for menu commands, input generators, file formats and more</p></figcaption></figure>

### Python Scripting and Jupyter Integration

* Python module (including Jupyter support) to load files, calculate orbitals, etc.
* Automate common tasks (e.g., load files, save graphics, animations)

### New and updated interfaces to external programs

* PySCF, Psi4, CP2k, APBS, LAMMPS, OpenMM
* Most interfaces use Python scripts to easily edit defaults and options
