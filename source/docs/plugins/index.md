(plugins)=

# Plugins and Python

Plugins are available to add a variety of functionality to Avogadro, enabling custom analysis, file formats, and integration with external tools.

Plugins can add a variety of functionality:

(plugins-features)=
| Symbol | Feature              | Functionality                       |
| ------ | -------------------- | --------------------------------- |
| ⚡      | Electrostatic Models | Models to calculate partial charges or [electrostatic potentials](tutorials-electrostatic-potential) |
| E      | Energy Models        | Additional models for the [AutoOptimization Tool](tools-autoopt-tool) |
| 📄     | File Formats         | Parsers for chemical file formats that Avogadro doesn't know |
| ⚛      | Input Generators     | Input file generators for computational chemistry programs |
| ☰     | Menu Commands         | Additional items for the menus that can carry out all sorts of tasks |

This section documents how to get and use the available plugins, which have all been written and uploaded by members of the Avogadro community.

:::{note}
For versions 2.0 or later, the distributed versions of Avogadro available from [the Install page](install) or the Releases page on GitHub should include everything needed for plugins to work seamlessly out-of-the-box.
If you have built Avogadro yourself, or are on Linux and are using the version provided by your Linux distribution, you will have to ensure certain requirements are fulfilled in order to use the plugins framework.
See [](plugins-python) for more details.
:::

Plugins are written as Python scripts or packages.
Information to help you write plugins yourself can be found in the **Develop** section under [Writing Plugins](develop-plugins).

```{toctree}
---
caption: Plugins
hidden: true
maxdepth: 1
---
manager
python
```
