(develop-avogadroapp)=

# Avogadro App

The `avogadroapp` project provides a fairly thin set of classes
around the `avogadrolibs` core. Among other things, it provides
scripts for bundling the desktop app on MacOS and Windows,
as well as code to open / save files, load language translations,
the about dialog, etc.

`aboutdialog`
: Displays the about dialog, including some versioning

`application`
: A minimal class mainly to handle `FileOpen` events from the operating system, e.g. to open files on launch

`avogadro`
: The main command-line program. Mostly handles initialization, including loading translations and the OpenGL context

`backgroundfileformat`
: Code for opening / saving files in a background thread to retain interactivity

`mainwindow`
: The main interface class. Handles loading tools, render types, etc. Most changes for `avogadroapp` probably involve this code.

`menubuilder`
: Code to load and sort the menu items from `avogadroapp` and plugin scripts

`renderingdialog`
: A settings dialog for various rendering options

`rpclistener`
: Code to handle [Remote Procedure Calls (RPC)](rpc) from external scripts or programs

`tdxcontroller`
: Contributed code to handle the 3DConnexion SpaceMouse device.

`tooltipfilter`
: A workaround to ensure tool buttons have tooltips

`viewfactory`
: Code to create multiple views on the same molecule
