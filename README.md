# cda — Coupled Dipole Approximation demos

Small repository demonstrating 1D and 2D coupled-dipole approximation variants:
- deterministic 1D
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
- 2D direct sums are slow for large Nx,Ny; examples use small grids by default.
- Mie and Lorentz-Drude scripts (if present) are optional and can be moved into cda/materials/.
