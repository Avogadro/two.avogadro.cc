# Introduction to Molecular Mechanics

Avogadro comes equipped with multiple different force fields. Below is general information regarding the force fields to help you select the best optimization method.

## UFF

UFF \(Universal Force Field\) is capable of reproducing the most structural feature across the periodic table. This force field can optimize the geometry for all elements, and does well with inorganic materials, and organometallic materials.

## MMFF94\(s\)

MMFF94 & MMFF94s \(designed by Merck\), is particularly good with organic compounds. MMFF94 has specifically been parameterized for alkanes, alkenes, alcohols, phenols, ethers, aldehydes, ketones, ketals, acetals, hemiketals, hemiacetals, amines, amides, peptide analogs, ureas, imides, carboxylic acids, esters, carboxylate anions, ammonium cations, thiols, mercaptans, disulfides, halides \(chlorides and fluorides\), imines, iminium cations, amine N-oxides, hydroxylamines, hydroxamic acids, amidines, guanidines, amidinium cations, guanidinium cations, imidazolium cations, aromatic hydrocarbons, and heteroaromatic compounds.

MMFF94 and MMFF94s use the same functional form to calculate the potential energy. They only differ in the Torsion and Out-Of-Plane bending parameters used. The 's' in MMFF94s stands for static and this set of parameters is more suited for tasks where the output is static.

These force fields also add electrostatic charges, and hydrogen bonds \(displayed below\).

![](../../_images/mmff94-s-.png)

## GAFF

GAFF \(General AMBER Force Field\) is often used for optimizing the geometries of drugs. AMBER \(Assisted Model Building with Energy Refinement\) is a common protein force field.

GAFF has specifically been parameterized for organic molecules made of C, N, O, H, S, P, F, Cl, Br, and I.

