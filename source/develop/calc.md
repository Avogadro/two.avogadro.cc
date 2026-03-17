(develop-calc)=

# Avogadro::Calc

The `calc` classes provide calculations for electrostatics (e.g., atomic partial charges) and force fields (i.e., energy calculators). They are structured similarly to the `io` classes in that there are modular subclasses which can be registered and accessed through two main classes.

- {doc}`ChargeManager <class/class_avogadro_1_1_calc_1_1_charge_manager>`
    - handles calculation of atomic partial charges, dipole moment, electrostatic potential
- {doc}`EnergyManager <class/class_avogadro_1_1_calc_1_1_energy_manager>`
    - handles calculation of energies, forces and gradients for optimizations

```{toctree}
:glob: true
:maxdepth: 1
:hidden: true

class/class_avogadro_1_1_calc*
```
