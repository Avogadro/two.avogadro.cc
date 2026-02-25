(develop-plugins-metadata)=

### Metadata and configuration

- Metadata that Avogadro needs to know in order to properly run a plugin was until now obtained dynamically by running the plugin
- Instead, metadata is now extracted from static TOML files
    - `plugin.json` is deprecated
- The static metadata for a plugin contains the following information:
    - The type of plugin
    - The features provided by the plugin, the types of each plugin feature (`file-formats`, `menu-commands` etc.), and various information about each feature e.g. what the display names and/or menu paths for each of those items should be
    - Info about the plugin's provenance that was previously in `plugin.json` e.g. author, version number
    - Whether or not the plugin wants a configuration to be recorded for it in the main Avogadro configuration file, and if so, what entries the config should have for the plugin
- The metadata file may be in the form of:
    - `pyproject.toml` – the normal project metadata file in use in the modern Python ecosystem
        - plugin metadata for consumption by Avogadro is listed in the `[tool.avogadro]` table
        - some information is read from the normal `[package]` table e.g. the author information
    - `avogadro.toml` – an Avogadro-specific metadata file
        - metadata is all stored at the top level of the file (see the examples in this repository)
- For Python plugins, it is recommended to use `pyproject.toml` as the metadata file.
    - If preferable, Python plugins may also use `avogadro.toml`. If both `avogadro.toml` and `pyproject.toml` are found in the plugin's directory, `avogadro.toml` will take precedence and `pyproject.toml` will be ignored.
- For non-Python plugins, `avogadro.toml` must be used.
