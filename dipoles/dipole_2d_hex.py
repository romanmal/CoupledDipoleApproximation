import numpy as np
from numpy.linalg import norm
from cda.units import lda_to_ev, k_from_lda
from cda.core import polarizability_drude, extinction_efficiency
from cda.plotting import plot_qext
import pandas as pd

def pnormangle(m, n):
    a1 = np.array([0.5, -0.5 * np.sqrt(3)])
    a2 = np.array([0.5, 0.5 * np.sqrt(3)])
    p = m * a1 + n * a2
    return norm(p), np.angle(p[0] + 1j * p[1])

def dipole_sum_2d_hex(k_vec, r, Nx=31, Ny=31, fctr=1/4):
    halfx = int(Nx//2)
    halfy = int(Ny//2)
    S = np.zeros_like(k_vec, dtype=np.complex128)
    for m in range(0, halfx+1):
        for n in range(0, halfy+1):
            if m == 0 and n == 0:
                continue
            pnorm, pang = pnormangle(m, n)
            if pnorm == 0:
                continue
            phase = np.exp(1j * k_vec * pnorm * r)
            term_pref = 4 * fctr if m == n else (0.5 * fctr if (m == 0 or n == 0) else 4 * fctr)
            term = term_pref * phase * (((1 - 1j * k_vec * pnorm * r) * (3 * (np.cos(pang))**2 - 1) / (pnorm * r)**3)
                                        + (k_vec**2) * (np.sin(pang))**2 / (pnorm * r))
            S += term
    return S

def run_2d_hex_demo(lat_consts_nm=[550], Nx=31, Ny=31, show=True):
    R = 50e-9
    wp_ev = lda_to_ev(np.array([415e-9]))[0]
    ldas = np.arange(350,801,1) * 1e-9
    w_ev = lda_to_ev(ldas)
    k_vec = k_from_lda(ldas)
    for lat_nm in lat_consts_nm:
        r = lat_nm * 1e-9
        S = dipole_sum_2d_hex(k_vec, r, Nx=Nx, Ny=Ny)
        alpha = polarizability_drude(w_ev, wp_ev, R, gamma_ev=0.43, S=S, radiative_correction=True)
        Qext = extinction_efficiency(alpha, k_vec, R)
        plot_qext(ldas*1e9, Qext, label=f"{lat_nm} nm")
    if show:
        import matplotlib.pyplot as plt
        plt.show()
    return pd.DataFrame({"lattice_nm": lat_consts_nm})
