import numpy as np
from cda.dipoles.dipole_1d import compute_dipole_sum_1d
from cda.units import lda_to_ev, k_from_lda
from cda.core import polarizability_drude, extinction_efficiency
from cda.plotting import plot_qext
import pandas as pd

def compute_dipole_sum_1d_random(k_vec, lattice_const_m, N=1001, random_delta_nm=10, rng=None):
    half = int(N//2)
    S = np.zeros_like(k_vec, dtype=np.complex128)
    rng = rng or np.random.default_rng()
    for i in range(1, half+1):
        rd_nm = int(lattice_const_m*1e9) + int(rng.integers(-random_delta_nm, random_delta_nm+1))
        rd = rd_nm * 1e-9
        denom_cubed = (i*rd)**3
        denom_linear = (i*rd)
        phase = np.exp(1j * k_vec * i * rd)
        term = phase * (((1j * k_vec * i * rd) - 1)/denom_cubed + (k_vec**2)/denom_linear)
        S += 2 * term
    return S

def run_1d_random_demo(show=True, seed=0):
    R = 50e-9
    wp_ev = lda_to_ev(np.array([415e-9]))[0]
    ldas = np.arange(300,801,1) * 1e-9
    w_ev = lda_to_ev(ldas)
    k_vec = k_from_lda(ldas)
    lat_consts_nm = [450, 500, 550]
    lat_consts = np.array(lat_consts_nm) * 1e-9
    rng = np.random.default_rng(seed)
    for a in lat_consts:
        S = compute_dipole_sum_1d_random(k_vec, a, N=1001, random_delta_nm=10, rng=rng)
        alpha = polarizability_drude(w_ev, wp_ev, R, gamma_ev=0.41, S=S)
        Qext = extinction_efficiency(alpha, k_vec, R)
        plot_qext(ldas*1e9, Qext, label=f"{int(a*1e9)} nm")
    if show:
        import matplotlib.pyplot as plt
        plt.show()
    return None
