# ML\_optimize\_hydro

This repository contains machine learning models useful for the acceleration and surroagtion of physical simulations in two spaitla dimensions, e.g. fluid dynamics computations.


## Generating fluctuating initial conditions (`predict_profiles`)
Certain models to describe the initial conditions of heavy-ion collisions can be computationally demanding. These notebooks explore building and training a Generative Adversarial Network (GAN) as a surrogate. 


## Optimizing total grid dimensions (`predict_radius`)
The equations of fluid dynamics give a macroscopic description of the long-wavelength behavior of a system. In particular, they are partial differential equations that evolve quantities such as the energy density, flow velocity, and stress tensor in space and time. 

Evolving these equations on a discrete lattice can be costly in 2 or 3 spatial dimensions, especially when small scales need to be resolved. Suppose that when the energy density drops below some threshold everywhere, we can stop the simulation. Then, it is advantageous if we can approximate ahead of time what the farthest possible distance from the coordinate origin of this low temperature surface. In that case, we can take a total lattice size which adds just enough padding to the edges. 

The basic concept is that the total size of the high-temperature region, after the system expands/cools, is a function of its initial temperature profile, and perhaps additional information such as the initial velocity profile, etc...

