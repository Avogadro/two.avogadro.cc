(develop-scripts-interfaces)=

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
<img src="../../_static/image.png" alt="1st">

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
<img src="../../_static/image-1.png" alt="2nd">

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

<img src="../../_static/image-2.png" alt="3rd">

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

<img src="../../_static/image-3.png" alt="4th">

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

<img src="../../_static/image-4.png" alt="5th">

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

<img src="../../_static/image-5.png" alt="6th">