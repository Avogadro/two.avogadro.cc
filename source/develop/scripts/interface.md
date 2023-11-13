(script-interfaces)=

# Script Interfaces

Both commands and input generator scripts can create user interfaces
using JSON syntax. For each option in the `userOptions` list, Avogadro
will create appropriate labels, menus, text boxes, check boxes, etc.

## Fixed String Lists (Pop-up menus)

Parameters that have a fixed number of mutually-exclusive string values
will be presented using a pop-up menu (combo box). Such a parameter can
be specified in the `userOptions` block as:

```json
{
  "userOptions": {
    "Parameter Name": {
      "type": "stringList",
      "values": ["Option 1", "Option 2", "Option 3"],
      "default": 0
    }
  }
}
```
![image](https://github.com/DHRUVJ2003/two.avogadro.cc/assets/91372908/94111870-2443-4119-a828-ecd6b17748e6)


Here, "Parameter Name" is the default label that will be displayed in
the GUI as a label next to the combo box. If you wish to have the label
differ from the JSON key, you can add a "label" key pair:

```json
"userOptions": {
  "element": {
    "type": "stringList",
    "label": "Metal",
    "values": ["Gold", "Silver", "Platinum"],
    "default": 0
  }
}
```
![image](https://github.com/DHRUVJ2003/two.avogadro.cc/assets/91372908/07c5cd56-3777-452a-ac7b-ab2cbad173d4)

Use of the "label" is optional, but encouraged, since it greatly
facilitates translation and localization (e.g., "color" vs. "colour").

The array of strings in values will be used as the available entries in
the combo box in the order they are written. The default parameter is a
zero-based index  into the values array and indicates which value should
be initially selected.

## Short Free-Form Text Parameters

A short text string can be requested (e.g. for the "title" of an
optimization) via:

```json
{
  "userOptions": {
    "Parameter Name": {
      "type": "string",
      "default": "blah blah blah"
    }
  }
}
```
This will add a blank text box to the GUI, initialized with the text
specified by default.

![image](https://github.com/DHRUVJ2003/two.avogadro.cc/assets/91372908/56437fe9-6735-4195-b39e-acb5b1f20d2b)


## Existing files

A script can ask for the absolute path to an existing file using the
following option block:

```json
{
  "userOptions": {
    "Parameter Name": {
      "type": "filePath",
      "default": "/path/to/some/file"
    }
  }
}
```
This will add an option to select a file to the GUI, initialized to the
file pointed to by default.

![image](https://github.com/DHRUVJ2003/two.avogadro.cc/assets/91372908/213e5724-d5fc-42a3-9a63-fdb1f43c147d)



## Integer Values

Scripts may request integer values from a specified range by adding a
user-option of the following form:

```json
{
  "userOptions": {
    "Parameter Name": {
      "type": "integer",
      "minimum": -5,
      "maximum": 5,
      "default": 0,
      "prefix": "some text ",
      "suffix": " units"
    }
  }
}
```
This block will result in a QSpinBox, configured as follows:

![image](https://github.com/DHRUVJ2003/two.avogadro.cc/assets/91372908/e49ebc6b-b526-4865-98e2-b09cbae7b6fa)
- minimum and maximum indicate the valid range of integers for the
  parameter.
- default is the integer value that will be shown initially.
- (optional) prefix and suffix are used to insert text before or after
  the integer value in the spin box. This is handy for specifying
  units. Note that any prefix or suffix will be stripped out of the
  corresponding entry in the call to scripts, and just the raw integer
  value will be sent.

## Floating-point values

Scripts may request floating-point values from a specified range by
adding:

```json
{
  "userOptions": {
    "Parameter Name": {
      "type": "integer",
      "minimum": -5,
      "maximum": 5,
      "default": 0,
      "prefix": "some text ",
      "suffix": " units"
          }
      }
  }
```

## Boolean Parameters

If a simple on/off value is needed, a boolean type option can be
requested:

```json
{
  "userOptions": {
    "Parameter Name": {
      "type": "boolean",
      "default": true,
    }
  }
}
```

This will result in a check box in the dynamically generated GUI, with
the initial check state shown in default.

![image](https://github.com/DHRUVJ2003/two.avogadro.cc/assets/91372908/6012c6ee-01d6-4108-ba4d-f1eb869a514b)
