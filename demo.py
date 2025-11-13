#!/usr/bin/env python3
"""
demo.py — quick CLI to run CDA variants

Usage:
    python demo.py --variant 1d
    python demo.py --variant 1d-random
    python demo.py --variant 2d-hex
    python demo.py --variant 2d-square
"""
import argparse
from cda.dipoles.dipole_1d import run_1d_demo
from cda.dipoles.dipole_1d_random import run_1d_random_demo
from cda.dipoles.dipole_2d_hex import run_2d_hex_demo
from cda.dipoles.dipole_2d_square import run_2d_square_demo

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--variant", choices=["1d","1d-random","2d-hex","2d-square"], default="1d")
    args = p.parse_args()
    if args.variant == "1d":
        run_1d_demo(show=True)
    elif args.variant == "1d-random":
        run_1d_random_demo(show=True, seed=42)
    elif args.variant == "2d-hex":
        run_2d_hex_demo(show=True, lat_consts_nm=[550], Nx=31, Ny=31)
    elif args.variant == "2d-square":
        run_2d_square_demo(show=True, lat_consts_nm=[550], Nx=31, Ny=31)

if __name__ == "__main__":
    main()
