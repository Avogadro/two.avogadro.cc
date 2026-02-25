(develop-plugins)=

# Plugins

:::{note}
For information on the installation and usage of plugins as a _user_, see the [section in the Guide](plugins).
:::

:::{versionchanged} 2.0
From the 2.0 release onwards, Avogadro's plugin framework has seen a significant overhaul, with a new plugin API, different metadata requirements, and changes to the infrastructure for sharing plugins.
If you are looking to write a plugin for Avogadro 1.90--1.103, details of the old API can be found [here](develop-scripts).
:::

## A brief outline of Avogadro's plugin API

### Feature types

- Plugins can provide any number of the following features:

| Feature type         | TOML key               | Purpose                       |
| -------------------- | ---------------------- | --------------------------------- |
| Electrostatic Models | `electrostatic-models` | Provide models for Avogadro to use in the calculation of partial charges and/or electrostatic potentials |
| Energy Models        | `energy-models`        | Provide models for Avogadro to use in the calculation of energies and gradients |
| File Formats         | `file-formats`         | Parse chemical file formats that Avogadro doesn't know |
| Input Generators     | `input-generators`     | Prepare input files for computational chemistry programs |
| Menu Commands        | `menu-commands`        | Add additional items for the menus that carry out various tasks |

### Basic requirements

- For now, plugins for Avogadro must be written in Python
    - Support for other languages may come at a later date; in particular, binary plugins would be of interest (though these would not be distributed via Avogadro's infrastructure due to security concerns)
- The installed form of a plugin used by Avogadro consists of a single directory bearing the plugin's name and containing a metadata file (see below) as well as all the plugin's source code in one of the three forms described below
- Plugins may only have `A-Z, a-z, 0-9, -` i.e. ASCII letters, numbers, and the hyphen minus, in their names (no Unicode, no underscores, no other punctuation or whitespace)
    - Underscores are substituted for hyphens in any situations where it is necessary, but the canonical name uses hyphens only
- All plugin files, and communication over the Avogadro-plugin interface, must be exclusively in UTF-8

### Plugin types

- There are **three sub-types** of Python plugin:
    1. Script(s)
    2. Python package
    3. Pixi project
- Note: unlike Avogadro 1.102 and earlier, single-file scripts with no metadata are no longer allowed – all scripts must be within their own folder with a metadata file, making them a proper plugin (even if the folder only contains a single script)

#### Script plugins (`pyscript`)

- A script plugin consists of one or more Python scripts collected into a single bundle in a folder, allowing for easy installation, deinstallation, management, and distribution
- Regardless of the number of scripts, a *single* metadata file (see below) is required for the plugin as a whole and must be located in the folder next to the scripts
- The plugin is not allowed to have any dependencies
- Script plugins are invoked by Avogadro by each script being run individually via the **script API**

#### Package plugins (`pypkg`)

- A package plugin for Avogadro is essentially a standard Python package as found in the wider ecosystem -- specifically, it consists of a directory that contains the source code for a Python *distribution* package, that can be built and installed by `pip`, `poetry`, `uv` etc.
- Metadata for Avogadro is generally contained in the package's `pyproject.toml`
- The plugin may use dependencies from the PyPI repository
- The plugin may use any structure for its source code that works for a Python package – the two most common structures are the so-called "flat" and "src" layouts
- Avogadro will install the plugin as a Python package to a Python virtual environment in one of two places (to be decided):
    1. The main Avogadro environment
        - Allows shared dependencies
        - Means code has to be written to account for the possibility that installation fails due to dependency conflicts
    2. A plugin-specific environment contained within the plugin's own folder
- Package plugins are invoked by Avogadro using the **package API**

#### Pixi project (`pypixi`)

- Pixi project plugins consist of a single directory containing a Pixi project, with a `pyproject.toml` file used as the Pixi environment manifest
- Metadata for Avogadro is generally contained in the project's `pyproject.toml`
- The plugin may use dependencies from the Conda ecosystem, as well as from the usual PyPI repository
- A plugin-specific Pixi environment is initialized for the plugin in its own directory, and all its dependencies are installed using Pixi
- Pixi plugins are also invoked by Avogadro using the **package API**

### The layout of Avogadro's local plugin directory

- Avogadro's data is stored under `<USERDATA>/OpenChemistry/Avogadro/`, where `<USERDATA>` is platform-specific. This location will be referred to as `.` throughout the rest of the document.
- Installed plugins are stored in subfolders under `./plugins/`:
    - `plugins/python/` for plugins written in Python


```{toctree}
---
caption: Writing Plugins
hidden: true
---
args
io
electrostatic-models
energy-models
file-formats
input-generators
menu-commands
user-options
metadata
sharing
```
