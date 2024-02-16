(develop-scripts-install)=

# Installing Script Plugins

Scripts can either be installed manually, by dragging to the Avogadro window:

![installing script](../_static/install-script.png)

Scripts can also be installed from GitHub repositories through the "Download Plugins…" command:

![plugin download](../_static/plugin-download.png)

## Directories

Avogadro will look for plugins either as individual files or subdirectories
in a few different paths, including system and user directories.

User-installed plugins are found within the Avogadro data folder, the location
of which is determined by
`QStandardPaths::standardLocations(QStandardPaths::AppLocalDataLocation)`:

- **Linux and BSD**: `~/.local/share/OpenChemistry/Avogadro`
- **macOS**: `~/Library/Application Support/OpenChemistry/Avogadro`
- **Windows**: `C:/Users/<USER>/AppData/Local/OpenChemistry/Avogadro`

Within this data folder, plugins are found in subdirectories organized by the
category of plugin.

![plugin subdirectories](../_static/plugin-directories.png)

Current plugin categories and their respective subdirectories:
- Scripts for calculating charges and electrostatic potentials – found in `charges`
- Scripts to add menu options for commands, which perform custom operations – found in `commands`
- Scripts that calculate energies and gradients on request by parts of Avogadro that run calculations – found in `energy`
- Scripts that generate input files for computational chemistry programs – found in `inputGenerators`
- Scripts that translate between different chemical file formats – found in `formatScripts`

On startup, each of these subdirectories will be scanned for individual
plugin files, as well as plugin "packages" – directories containing mutliple
files as well as a `plugin.json` with information about the plugin.

```{warning}
The main data folder should not be used for plugin files and plugins saved
there will not be loaded.

Plugins must be saved within the appropriate subdirectory for their type.
```

## Plugin Packages and Repositories

Since some plugins may require additional scripts or resources to function,
they can be installed as entire self-contained directory to make a "package".

- [avogadro-cclib](https://github.com/OpenChemistry/avogadro-cclib) - [reads files](formats) through the `cclib` Python module and needs a `utils.py` helper script
- [avogadro-rdkit](https://github.com/ghutchis/avogadro-rdkit) - packages multiple [command](commands) scripts together since they all use the `rdkit` package

All repositories must include a `plugin.json` file, which is used by Avogadro
to indicate the actual plugin scripts (e.g., multiple [commands](commands))
as well as the Download Plugins… command to provide information to the user:

```json
{
  "author": "Geoffrey Hutchison",
  "version": 1.0,
  "url": "https://github.com/ghutchis/avogadro-scikit-nano",
  "name": "avogadro-scikit-nano",
  "description": "Generate carbon nanomaterial using scikit-nano",
  "type": "commands",
  "commands": [
    { "name": "SWNT", "command": "swnt.py" },
    { "name": "MWNT", "command": "mwnt.py" }
  ]
}
```

Required sections:
- `author`: a user-visible attribution of the script
- `version`: a version number of the script (which is ignored based on GitHub tags or releases)
- `url`: the URL of the GitHub repository
- `name`: the name of the plugin. Initial `avogadro-` prefix will be ignored by the Download Plugins… dialog.
- `description`: a brief description of the plugin
- `type`: the category of plugin script, including:
  - `charges` for [charge / electrostatics models](charges)
  - `commands` for [menu commands](commands)
  - `energy` for [energy / force field models](energy)
  - `formats` for [file formats](formats)
  - `generators` for [input generators](generators)
- `commands`: a list of key/value pairs to indicate a potential `name` and the `command` filename for the script.

Note that any files **not** listed in the `commands` list will be ignored by
Avogadro during launch.

## Adding to the Plugin Directory

When you are ready to add your plugin repository to the download list, create a release and submit a 
pull request to:
https://github.com/Avogadro/plugins/blob/master/repositories.txt

Someone will check your plugin and approve the addition to the list of approved repositories. An 
automated script runs daily to generate the cached information on the plugin repositories, so it may
not appear immediately.

Suggestions for a more complete plugin repository system are welcome.
