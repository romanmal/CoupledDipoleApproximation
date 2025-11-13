import numpy as np
from cda.units import lda_to_ev, k_from_lda
from cda.core import polarizability_drude, extinction_efficiency
from cda.plotting import plot_qext
import pandas as pd

def dipole_sum_2d_square(k_vec, r, Nx=31, Ny=31, fctr=1.0):
    halfx = int(Nx//2)
    halfy = int(Ny//2)
    S = np.zeros_like(k_vec, dtype=np.complex128)
    for x in range(0, halfx+1):
        for y in range(0, halfy+1):
            if x == 0 and y == 0:
                continue
            dist = r * np.sqrt(x**2 + y**2)
            ang = np.arctan2(y, x)
            # multiplicity for (±x, ±y)
            mult = 4
            phase = np.exp(1j * k_vec * dist)
            term = mult * fctr * phase * (
                ((1 - 1j * k_vec * dist) * (3 * (np.cos(ang))**2 - 1) / (dist**3)) +
                (k_vec**2) * (np.sin(ang))**2 / dist
            )
            S += term
    return S

def run_2d_square_demo(lat_consts_nm=[550], Nx=31, Ny=31, show=True):
    R = 50e-9
    wp_ev = lda_to_ev(np.array([415e-9]))[0]
    ldas = np.arange(350,801,1) * 1e-9
    w_ev = lda_to_ev(ldas)
    k_vec = k_from_lda(ldas)
    for lat_nm in lat_consts_nm:
        r = lat_nm * 1e-9
        S = dipole_sum_2d_square(k_vec, r, Nx=Nx, Ny=Ny)
        alpha = polarizability_drude(w_ev, wp_ev, R, gamma_ev=0.41, S=S, radiative_correction=True)
        Qext = extinction_efficiency(alpha, k_vec, R)
        plot_qext(ldas*1e9, Qext, label=f"{lat_nm} nm")
    if show:
        import matplotlib.pyplot as plt
        plt.show()
    return pd.DataFrame({"lattice_nm": lat_consts_nm})
