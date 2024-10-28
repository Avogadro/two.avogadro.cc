(develop-structure)=

# Project Structure

## What is Open Chemistry?

[Open Chemistry](https://www.openchemistry.org/) is an umbrella for the development of several open-source chemical tools.
Avogadro is its primary subproject, but it also oversees the [Chemical JSON](https://github.com/OpenChemistry/chemicaljson) file format as well as [a bunch of other cool stuff](https://github.com/orgs/OpenChemistry/repositories).

The Avogadro desktop application is made up primarily of the `avogadrolibs` module, which does all the behind-the-scenes work, and the `avogadroapp` which provides a GUI on top. This split allows functions from `avogadrolibs` to be available in Python modules, for example to read chemistry files, generate molecular orbital surfaces.

In practice, most functionality and features are provided by `[avogadrolibs](https://github.com/OpenChemistry/avogadrolibs)` and particularly by various plugin classes.

The main project uses various other Open Chemistry modules to function.

[avogadroapp](https://github.com/OpenChemistry/avogadroapp)
: Code to handle [the desktop app events and interface](develop-avogadroapp)

[avogadro-i18n](https://github.com/OpenChemistry/avogadro-i18n)
: Language translations and localization handled through [Weblate](https://hosted.weblate.org/engage/avogadro/)

[avogenerators](https://github.com/OpenChemistry/avogenerators)
: Scripts providing input generator dialogs for various computational packages such as Gaussian, Orca, etc.

[crystals](https://github.com/OpenChemistry/crystals)
: Example crystal structures provided through File ⇒ Import ⇒ Crystal

[fragments](https://github.com/OpenChemistry/fragments)
: Common inorganic ligands and functional groups provided through the Template Tool

[molecules](https://github.com/OpenChemistry/molecules)
: Common molecules provided through Build ⇒ Insert ⇒ Molecule
