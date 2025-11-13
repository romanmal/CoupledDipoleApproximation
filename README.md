# cda — Coupled Dipole Approximation for Light Scattering Particles

Implementation of 1D and 2D coupled-dipole approximation based on my MSc thesis in Nanotechnology (2020), photonics. The thesis can be found at https://hdl.handle.net/11250/2778159.

The variants implemented are
- 1D array of particles with fixed periodicities
- random-periodicity 1D
- 2D hexagonal lattice
- 2D square lattice

Quickstart
1. Create and activate a virtualenv
2. pip install -r requirements.txt
3. Run a quick demo:
   python demo.py --variant 1d
   python demo.py --variant 1d-random
   python demo.py --variant 2d-hex
   python demo.py --variant 2d-square

Repository layout
- demo.py — single-file CLI to run variants
- cda/units.py, cda/core.py — shared utilities and physics
- cda/dipoles/* — implementations per geometry
- cda/plotting.py — small plotting helpers
- examples/ — example scripts
- tests/ — lightweight pytest checks

Notes
- 2D direct sums are slow for large Nx,Ny; examples use small grids by default
