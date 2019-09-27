# ml_optimize_hydro

This repository serves as a set of machine learning models useful for the acceleration of fluid dynamics computations.

## Optimizing total grid dimensions
These are useful tools for approximating the maximum grid dimensions necessary to capture the high-temperature regions of an expanding system. In principle, rather than training the models using simulation data from viscous fluid dynamics, one could use any physical description of the system to train the machine learning models. 
The basic concept is that the total size of the high-temperature region, after the system expands/cools, is a function of its initial temperature profile, and perhaps additional information such as the initial velocity profile, etc...

