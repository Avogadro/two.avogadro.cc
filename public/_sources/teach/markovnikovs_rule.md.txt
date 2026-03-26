# Markovnikov's Rule

Investigate the stability of reactions using Markovnikov's rule.

## Task

Build a propene molecule and optimize its geometry. Compare the relative energy of bromine-hydrogen substitution at either the 1-carbon or 2-carbon of the carbon-carbon double bond. Which of these two bromopropane compounds will be the major product of a propene bromination reaction?

![](../_static/Markovnikovs_rule.png)

## Solution

![](../_static/Markovnikovs_rule_mechanistic.png)

Results of relative energies expressed in kJ/mol (need confirmation in literature).

| Force field | Intermediate primary carbocation (1') | Intermediate secondary carbocation (2') | 1-bromopropane (1) | 2-bromopropane (2) |
| ----------- | ----------- | ------------- | ---------- | ---------- | 
| Ghemical    | -2.24       | -2.06         | -2.39      | -1.87 |
| MMFF94      | -9.88       | -3.84         | -8.96      | +2.70 |
| UFF         | +4.05       | +3.63         | +4.15      | +4.86 |

UFF data is considered in this case, the secondary carbocation intermediate requires less energy (2') than the primary carbocation intermediate (1') (resp. 3.6 vs 4 kJ/mol). So compound (2) will be the major form. This is called the Markovnikov’s rule: “the major product of the addition of HX (where X is some atom more electronegative than H, the bromine in our case) to an alkene (here the propene) has the hydrogen atom in the less substituted position and X in the more substituted position”. Mechanisms which avoid the carbocation intermediate such as the presence of dialkyl peroxides will reverse the reaction result and compound (1) becomes the major product (Anti-Markovnikov rule).

## See also

[Alkene Isomers](alkene_isomers)

## Further reading

[Markovnikov's rule (wikipedia)](https://en.wikipedia.org/wiki/Markovnikov's_rule)
