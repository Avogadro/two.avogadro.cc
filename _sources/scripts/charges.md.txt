(script-charges)=

# Charges / Electrostatics

Avogadro allows scripts to translate between formats which Avogadro already
handles and new formats (e.g., to use packages like cclib).

The script must handle the following command line arguments:

- `--metadata` Print metadata describing the script
- `--display-name` Print the name to display in user options
- `--lang en` Optionally respond to language translation codes
- `--charges` Calculate atomic partial charges for a molecule
- `--potential` Calculate the electrostatic potentail for a molecule
on a supplied set of points (e.g., a molecular surface)

With the exception of `--metadata` and `--display-name` options, charge scripts
can respond to either `charge` or `potential` requests or both. For example,
many partial charge models approximate the electrostatic potential given by
the point charges, which is handled by Avogadro internally. On the other hand,
a machine learning model may only handle the electrostatic potential grid
directly, but not assign atomic partial charges.

## Identify the Script with `--metadata`

Running the script with the `--metadata` option should print a JSON object
of the following form:

```
{
  "inputFormat": "mol",
  "identifier": "Unique Name"
  "name": "User-Friendly Name",
  "description": "Description of method or citation.",
  "charges": True,
  "potential": False,
  "elements": "1,6-9"
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
- `charges` indicates whether the script can provide atomic partial charges.
- `potential` indicates whether the script can provide electrostatic potential
  at specified points (supplied by Avogadro).
- `elements` is a list indicating the atomic numbers supported by the method.
  Both commas `1, 6, 7` and ranges `1-86` are supported.

Optional members are:
: - `description`

## Calculating Atomic Partial Charges with `--charge`

Many chemists prefer to think of
[atomic partial point charges](https://en.wikipedia.org/wiki/Partial_charge).
For that reason, these methods are common.

Avogadro will provide the molecule on the standard input in the format requested
by the `inputFormat` metadata.

Calculate charges and print them in the same order as the atoms on the standard
output.

For example, a script requesting the `xyz` format will get water as:

```
3

O          0.93364        0.09813        0.00687
H          1.90153        0.06280        0.03699
H          0.65479       -0.60815        0.60884
```

And return:
```
   -0.56095360
    0.28047667
    0.28047692
```

No particular numeric format is required in the standard output.

## Generating Electrostatic Potentials with `--potential`

Some programs can directly calculate the electrostatic potential for a molecule
at given points (e.g., on the solvent-excluded surface).

Since Avogadro must provide both the molecular data and the list of points,
JSON is supplied on the standard input. The molecular file is provided with
the key used by `inputFormat`. The points are supplied in an array of
floating point values with the `points` key.

For example our water molecule might be evaluated at the two points
(0.0, 0.0, 0.0) and (1.0, 0.0, 0.0):

```
{
    "xyz": "3

O          0.93364        0.09813        0.00687
H          1.90153        0.06280        0.03699
H          0.65479       -0.60815        0.60884",
    "points": [ 0.0, 0.0, 0.0, 1.0, 0.0, 0.0 ]
}
```

Again, the script should simply compute the electrostatic potential at these
points and print the values on the standard output:

```
   0.1234
   -0.5678
```

These are completely random values for illustration purposes.