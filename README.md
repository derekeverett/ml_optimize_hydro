# ML\_optimize\_hydro

This repository serves as a set of machine learning models useful for the acceleration of fluid dynamics computations.

## Optimizing total grid dimensions
These are useful tools for approximating the maximum grid dimensions necessary to capture the high-temperature regions of an expanding system. 

In principle, rather than training the models using simulation data from viscous fluid dynamics, one could use any physical description of the system to train the machine learning models. 

The basic concept is that the total size of the high-temperature region, after the system expands/cools, is a function of its initial temperature profile, and perhaps additional information such as the initial velocity profile, etc...

## Fluid Dynamic Example
The equations of fluid dynamics give a macroscopic description of the long-wavelength behavior of a system. In particular, they are partial differential equations that evolve quantities such as the energy density, flow velocity, and stress tensor in space and time. 

Evolving these equations on a discrete lattice can be costly in 2 or 3 spatial dimensions, especially when small scales need to be resolved. Suppose that when the energy density drops below some threshold everywhere, we can stop the simulation. Then, it is advantageous if we can approximate ahead of time what the farthest possible distance from the coordinate origin of this low temperature surface. In that case, we can take a total lattice size which adds just enough padding to the edges. 