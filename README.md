# hBN-crack-initiation
This repository contains 'sample' LAMMPS input scripts for molecular dunamics simulation and stress field analysis, various python post processing scripts, and other key files, including initial atomistic model of hBN that work as input for the different scripts - which are part of my project to analyze the 'principal' stress concentration, structural distortion, and maximum bond strength in the hBN model at the onset of failure under tensile test.
The files are as follows:

A) LAMMPS input scripts: full.in, rerun.in, reruncheck.in

B) Python post processing tools: principal.py, principal_absolute_y.py

C) The bond strength.ovito, and concentration b.ovito, are visualization files (for Ovito tool) that use the results of post-processing (hBNrerunprincipalstress.814673.atom is the atomic coordinate data file before fracture - where the calculated properties during postprocessing have been added in the form of a LAMMPS structure data file to be viewed in Ovito), in order to determine the maximum principal stress along any bond and create concentration maps.

