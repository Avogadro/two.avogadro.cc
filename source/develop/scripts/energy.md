(develop-scripts-energy)=

# Energy / Force Fields

Avogadro allows scripts to calculate energies and gradients for optimizing geometry.

The script must handle the following command line arguments:

- `--metadata` Print metadata describing the script
- `--display-name` Print the name to display in user options
- `--lang en` Optionally respond to language translation codes
- `--file FILE` Calculate energies and gradients for a particular molecule

With the exception of `--metadata` and `--display-name` options

## Identify the Script with `--metadata`

Running the script with the `--metadata` option should print a JSON object
of the following form:

```json
{
  "inputFormat": "pdb",
  "identifier": "Unique Name"
  "name": "User-Friendly Name",
  "description": "Description of method or citation.",
  "elements": "1,6-9"
  "unitCell": False,
  "gradients": True,
  "ion": False,
  "radical": False,
}
```

Details:

- `inputFormat` indicates the molecular file format that Avogadro should
supply to the script. Allowed values are `"cml"`, `"cjson"`, `"pdb"`, `"sdf"`
or `"xyz"`. Instead of `"sdf"`, the extensions `"mdl"` or `"mol"` are also
allowed.
- `identifier` is a unique identifier. The value must only be unique amongst
  script charges, since it is used internally.
- `name` is a user-friendly name for the method, which will be used in menus.
- `description` is an *optional* description of the method, along with any
 relevant help text for users.
- `elements` is a list indicating the atomic numbers supported by the method.
  Both commas `1, 6, 7` and ranges `1-86` are supported.
- `unitCell` is either `True` or `False` as to whether systems with lattice vectors are supported by the method.
- `gradients` indicates `True` if analytical gradients will be calculated by the method or `False` if Avogadro should calculate numeric gradients.
- `ion` indicates `True` if the method can handle systems with non-zero total charge (e.g., cations, anions, etc.)
- `radical` indicates `True` if the method can handle systems with unpaired spins (i.e., spin multiplicity beyond singlet).

Optional members are:
: - `description`

Make sure to specify the `elements` list correctly. Avogadro will automatically
exclude a script in the list of available methods if a molecule contains
elements not in the list (e.g., if it does not support metals), or based on the `unitCell`, `ion`, and `radical` fields.

## Calculating Energies and Gradients

Avogadro will write a temporary file in the specified file format and supply the filename when calling the script, e.g. `script.py -f tempfile.mol`.

For example a script using Open Babel might use code like this:

```python
# we declared "inputFormat": "cml" in the metadata
def run(filename):
    # we get the molecule from the supplied filename
    #  in cjson format (it's a temporary file created by Avogadro)
    mol = next(pybel.readfile("cml", filename))
 
    ff = pybel._forcefields["uff"]
    success = ff.Setup(mol.OBMol)
    if not success:
        # should never happen, but just in case
        sys.exit("UFF force field setup failed")
```

Another example is to use cjson and get elements and coordinates:

```python
def run(filename):
    # we get the molecule from the supplied filename
    #  in cjson format (it's a temporary file created by Avogadro)
    with open(filename, "r") as f:
        mol_cjson = json.load(f)
 
    # get the atomic numbers
    atoms = np.array(mol_cjson["atoms"]["elements"]["number"])
    # get the coordinates in a list of [ [x, y, z], [x, y, z] … ]
    coord_list = mol_cjson["atoms"]["coords"]["3d"]
    coordinates = np.array(coord_list, dtype=float).reshape(-1, 3)
```

After reading coordinates from the tempory filename on the command-line arguments, Avogadro will supply updated coordinates through standard input and expect energies and gradients on the standard output.

```python
    # we loop forever - Avogadro will kill the process when done
    num_atoms = len(mol.atoms)
    while True:
        # read new coordinates from stdin
        for i in range(num_atoms):
            coordinates = np.fromstring(input(), sep=" ")
            atom = mol.atoms[i]
            atom.OBAtom.SetVector(coordinates[0], coordinates[1], coordinates[2])
 
        # update the molecule geometry for the next energy
        ff.SetCoordinates(mol.OBMol)
 
        # first print the energy of these coordinates
        energy = ff.Energy(True)  # in kJ/mol
        print("AvogadroEnergy:", energy)  # in kJ/mol

        # now print the gradient on each atom
        print("AvogadroGradient:")
        for atom in mol.atoms:
            grad = ff.GetGradient(atom.OBAtom)
            print(-1.0*grad.GetX(), -1.0*grad.GetY(), -1.0*grad.GetZ())
```

Note that Avogadro expects energies and gradients with the indicated tags:

`AvogadroEnergy: [energy]`

```
AvogadroGradient:
x y z
x y z
x y z
x y z
…
```

## Unit Cells, Total Charge, and Spin Multiplicity

If your method involves unit cells, total charge, or spin multiplicity, the `cjson` format is likely your best option.

### Lattice Vectors and Fractional Coordinates

The `cjson` format from Avogadro will provide both real-space Cartesian coordinates as `cjson["atoms"]["coords"]["3d"]` and fractional coordinates as `cjson["atoms"]["coords"]["3dFractional"]`. For both cases, the coordinates are supplied as a 1D array, which can be reshaped via `numpy`, e.g. `np.array(coord_list, dtype=float).reshape(-1, 3)`.

The unit cell parameters and lattice vectors are also available in `cjson`:

```json
  "unitCell": {
    "a": 4.0862,
    "alpha": 90.0,
    "b": 4.0862,
    "beta": 90.0,
    "c": 4.0862,
    "cellVectors": [
      4.0862,
      0.0,
      0.0,
      0.0,
      4.0862,
      0.0,
      0.0,
      0.0,
      4.0862
    ],
    "gamma": 90.0
  }
```

For example, if your script needs the lattice vectors, you can use `cjson["unitCell"]["cellVectors"]` to get a 1D list of the vectors and can reshape via `np.array(cell_list, dtype=float).reshape(3,3)`. Alternatively, you can access:

- `a = cjson["unitCell"]["a"]`
- `b = cjson["unitCell"]["a"]`
- `c = cjson["unitCell"]["a"]`
- `alpha = cjson["unitCell"]["alpha"]`
- `beta = cjson["unitCell"]["beta"]`
- `gamma = cjson["unitCell"]["gamma"]`
