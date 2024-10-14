(develop-structure)=

# Project Structure

## What is Open Chemistry?

[Open Chemistry](https://www.openchemistry.org/) is an umbrella for the development of several open-source chemical tools.
Avogadro is its primary subproject, but it also oversees the [Chemical JSON](https://github.com/OpenChemistry/chemicaljson) file format as well as [a bunch of other cool stuff](https://github.com/orgs/OpenChemistry/repositories).

The Avogadro desktop application is made up primarily of the `avogadrolibs` module, which does all the behind-the-scenes work, and the `avogadroapp` module, which provides a GUI on top.
In practice,

 relies on various other Open Chemistry modules to function. 
