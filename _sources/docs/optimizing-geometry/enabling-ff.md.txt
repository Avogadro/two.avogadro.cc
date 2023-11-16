# Enabling additional force fields

Avogadro2 comes equipped with a Lennard-Jones (LJ) force field, but you may wish to use a [different force field](force-fields) that is more suitable for your chemical system. These force fields are only enabled through interfaces to other programs. This includes:

- The UFF and MMFF94 force fields via openbabel.
- The GFN-FF force field via xtb-python.

One of the easiest ways to do this is to create a conda environment that includes the external program(s) you require.

## Creating an avogadro conda environment

Assuming conda is already installed on your system, the following will create a new environment named avogadro that contains both the openbabel and xtb-python packages.

	conda create -c conda-forge --name avogadro openbabel xtb-python

When desired, this environment can then be activated as:

	conda activate avogadro

```{warning}
Additional packages may need to be added to your conda environment in order for the force field scripts to run. For example, xtb-python may require the typing_extensions package.
```

## Setting the Python path

It is also necessary to set the Python path correctly for Avogadro to be able to interface with the Python modules. To do this, go to the "Extensions" menu and select "Set Python Path...". 

![](../../_static/python-path.png)

In the dialogue box, browse to (or copy and paste) the Python executable from the corresponding conda environment. Assuming a Linux or macOS system, you can find this by typing `which python` from a terminal (with the conda environment active). Once this is set, select OK.

![](../../_static/set-path.png)

You must now restart Avogadro for changes to take effect. If you now go to the "Extensions" menu, and under "Calculate", select "Setup Force Field..." you should be able to select the additional force fields.

![](../../_static/ff-selector.png)

