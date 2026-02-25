(develop-plugins-sharing)=

### The online plugin repository/index

- The Avogadro team continues to provide a central index of plugins, that can then be browsed and installed from within the plugin manager in the Avogadro UI
- The index has until now been hosted at https://avogadro.cc/plugins.json; the future location has yet to be decided
- The index is in future to be regularly updated in an automated fashion from the `repositories.toml` file in the GitHub repository at https://github.com/Avogadro/plugins
- Contributions of open-source plugins to the index is most welcome, and are made by opening a pull request that adds information on the plugin to the `repositories.toml` file in the `Avogadro/plugins` repo
- Each plugin listed on the index has its own table within `repositories.toml`. Each plugin has to specify (at minimum, suggestions welcome):
    - The git repository
    - The specific commit
    - Possibly a SHA256 hash that Avogadro can use to check the plugin files after download
    - The type of plugin, one of:
        - `py-scripts`
        - `py-pkg`
        - `py-pixi`
- Updates to plugins are likewise submitted to the index by submitting a PR to update the commit listed in `repositories.toml`
    - This improves security in comparison to the old index as the code for the plugin can't just be changed and delivered to all future plugin users without approval from the Avogadro team
- The new API thus uses a new file to hold information on the plugin repositories; this means we can keep the old one for a little while if we like, to avoid breaking plugins for older versions just yet
