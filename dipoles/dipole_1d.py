import numpy as np
from cda.units import lda_to_ev, k_from_lda
from cda.core import polarizability_drude, extinction_efficiency
from cda.plotting import plot_qext, plot_lattice_peaks
import pandas as pd

def compute_dipole_sum_1d(k_vec, lattice_const_m, N=1001):
    half = int(N//2)
    S = np.zeros_like(k_vec, dtype=np.complex128)
    for i in range(1, half+1):
        rd = lattice_const_m
        denom_cubed = (i*rd)**3
        denom_linear = (i*rd)
        phase = np.exp(1j * k_vec * i * rd)
        term = phase * (((1j * k_vec * i * rd) - 1)/denom_cubed + (k_vec**2)/denom_linear)
        S += 2 * term
    return S

def run_1d_demo(show=True):
    R = 50e-9
    wp_ev = lda_to_ev(np.array([415e-9]))[0]
    ldas = np.arange(300,801,1) * 1e-9
    w_ev = lda_to_ev(ldas)
    k_vec = k_from_lda(ldas)
    lat_consts_nm = [450, 500, 550, 600]
    lat_consts = np.array(lat_consts_nm) * 1e-9
    latres = []
    for a in lat_consts:
        S = compute_dipole_sum_1d(k_vec, a, N=1001)
        alpha = polarizability_drude(w_ev, wp_ev, R, gamma_ev=0.41, S=S)
        Qext = extinction_efficiency(alpha, k_vec, R)
        plot_qext(ldas*1e9, Qext, label=f"{int(a*1e9)} nm")
        idx = (np.abs(ldas - a)).argmin()
        low = max(0, idx-50); high = min(len(Qext), idx+50)
        peak = ldas[Qext[low:high].argmax()]
        latres.append(peak)
    if show:
        import matplotlib.pyplot as plt
        plt.show()
    plot_lattice_peaks(np.array(lat_consts_nm), np.array(latres)*1e9)
    if show:
        import matplotlib.pyplot as plt
        plt.show()
    return pd.DataFrame({"lattice_nm": lat_consts_nm, "peak_nm": np.array(latres)*1e9})
