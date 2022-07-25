(api)=

# Library API

Avogadro libraries can be used from both C++ and Python interfaces.

The Avogadro libraries are developed to support the Avogadro2 application, and
provide liberally BSD-licensed, open-source reusable components for both C++ and Python. At its core it is a platform for developing molecular visualization, editing and interactive simulation applications. This is achieved using a collection of libraries, along with a plugin interface allowing the platform to be easily extended and used in a variety of environments.

## Main Classes

The Avogadro libraries are implemented as a set of libraries, where all classes
are implemented in the Avogadro `namespace`, and each library uses a namespace
to distinguish members of that library. Include directories are also divided
up by library, resulting in classes such as `Avogadro::Core::Molecule` in the
include file `<avogadro/core/molecule.h>`. Some of the main classes that are
useful to get acquainted with are:

- Core::Molecule : The base molecule class, for representing molecules.
  - Core::Atom : Class representing atoms in a molecule.
  - Core::Bond : Class representing bonds in a molecule.
- Io::FileFormatManager : Convenience functions for file format wrangling.
- Io::FileFormat : Base class for all file format readers and writers.
  - Io::CjsonFormat : Chemical JSON format reader and writeer.
- Rendering::Scene : Class managing the main scene graph used for rendering.
- Rendering::Drawable : Base class for drawable items in the scene.
  - Rendering::SphereGeometry : Drawable item for spheres.
  - Rendering::CylinderGeometry : Drawable item for cylinders.
- QtGui::PeriodicTableView : A periodic table widget.
- QtOpenGL::GLWidget : Provides an OpenGL widget for 3D molecule rendering.

If you wish to extend Avogadro the main base classes are:

- QtGui::ScenePlugin : Generate geometry to be rendered in the scene.
- QtGui::ToolPlugin : Base class for mouse interaction, editing, etc.
- QtGui::ExtensionPlugin : Base class for dialog/menu extensions.

Many examples of each can be found in the `avogadro/qtplugins/` subdirectories.

```{toctree}
---
caption: API
maxdepth: 2
hidden: true
---

rpc
classlist
```
