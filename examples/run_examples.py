#!/usr/bin/env python3
"""
examples/run_examples.py

Run all CDA demo variants with small defaults, save plots and print peak tables.

Usage:
    python examples/run_examples.py
"""

import os
from pathlib import Path
import matplotlib.pyplot as plt

# ensure examples folder exists
out_dir = Path(__file__).resolve().parent
fig_dir = out_dir / "figs"
fig_dir.mkdir(parents=True, exist_ok=True)

# import demo functions from the package
from cda.dipoles.dipole_1d import run_1d_demo
from cda.dipoles.dipole_1d_random import run_1d_random_demo
from cda.dipoles.dipole_2d_hex import run_2d_hex_demo
from cda.dipoles.dipole_2d_square import run_2d_square_demo

def run_and_save_1d():
    print("Running 1D deterministic demo...")
    df = run_1d_demo(show=False)  # returns DataFrame with peaks
    plt.gcf().savefig(fig_dir / "1d_deterministic_qext.png", dpi=200, bbox_inches="tight")
    print("1D deterministic peaks (nm):")
    print(df)
    plt.close("all")

def run_and_save_1d_random():
    print("Running 1D random demo...")
    run_1d_random_demo(show=False, seed=42)
    plt.gcf().savefig(fig_dir / "1d_random_qext.png", dpi=200, bbox_inches="tight")
    print("Saved 1d_random_qext.png")
    plt.close("all")

def run_and_save_2d_hex():
    print("Running 2D hex demo (small grid)...")
    df = run_2d_hex_demo(lat_consts_nm=[550], Nx=31, Ny=31, show=False)
    plt.gcf().savefig(fig_dir / "2d_hex_qext.png", dpi=200, bbox_inches="tight")
    print("2D hex demo done. DataFrame:")
    print(df)
    plt.close("all")

def run_and_save_2d_square():
    print("Running 2D square demo (small grid)...")
    df = run_2d_square_demo(lat_consts_nm=[550], Nx=31, Ny=31, show=False)
    plt.gcf().savefig(fig_dir / "2d_square_qext.png", dpi=200, bbox_inches="tight")
    print("2D square demo done. DataFrame:")
    print(df)
    plt.close("all")

def main():
    run_and_save_1d()
    run_and_save_1d_random()
    run_and_save_2d_hex()
    run_and_save_2d_square()
    print(f"All figures saved to: {fig_dir}")

if __name__ == "__main__":
    main()
