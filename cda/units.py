import numpy as np
from numpy import pi

def lda_to_ev(lda_m):
    """Convert wavelength(s) in meters to photon energy in eV (rounded)."""
    c = 3e8
    h = 6.62607015e-34
    e0 = 1.602176634e-19
    eV = (h * c) / lda_m / e0
    return np.round(eV, 2)

def k_from_lda(lda_m):
    """Wavevector k = 2*pi / lambda (vectorized)."""
    return 2 * pi / lda_m
