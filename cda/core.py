import numpy as np

def polarizability_drude(w_ev, wp_ev, R_m, gamma_ev=0.41, A_factor=None, S=None, radiative_correction=False):
    """
    Drude-like polarizability. If S provided, included in denominator.
    """
    if A_factor is None:
        A = 0.5 * wp_ev * (R_m ** 3)
    else:
        A = A_factor
    denom = (w_ev - wp_ev + 1j * gamma_ev)
    if S is not None:
        denom = denom + A * S
    a_small = -A / denom
    if radiative_correction and S is not None:
        return a_small / (1 - a_small * S)
    return a_small

def extinction_efficiency(alpha, k_vec, R_m):
    """Qext = Cext / (pi R^2) with Cext = 4*pi*k*Im(alpha)."""
    Cext = 4 * np.pi * k_vec * np.imag(alpha)
    Qext = Cext / (np.pi * R_m**2)
    return Qext
