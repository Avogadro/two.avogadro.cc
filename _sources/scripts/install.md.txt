(script-install)=

# Installing Script Plugins

Scripts can either be installed manually, by dragging to the Avogadro window:

![installing script](/_images/install-script.png)

Scripts can also be installed from GitHub repositories through the "Download Plugins…" command:

![plugin download](/_images/plugin-download.png)

## Directories

Avogadro will look for plugins either as individual files or subdirectories
in a few paths, including system and user directories. Each type of plugin
should be in the corresponding subdirectory, e.g.:

![plugin subdirectories](/_images/plugin-directories.png)

The main directory for installing plugins is determined by `QStandardPaths::standardLocations(QStandardPaths::AppLocalDataLocation)`:

- **Linux and BSD**: `~/.local/share/avogadro/`
- **macOS**: `Library/Application\ Support/OpenChemistry/Avogadro`
- **Windows**: `C:/Users/USER/AppData/Local/Avogadro`

Inside each of these paths, subdirectories for each category of plugin will be
scanned for both individual files and directories containing `plugin.json` files
indicating a plugin "package."

## Plugin Packages and Repositories

Since some plugins may require additional scripts or resources to function,
they can be installed as an entire directory.

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
