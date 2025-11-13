import numpy as np
from cda.units import lda_to_ev, k_from_lda
from cda.dipoles.dipole_1d import compute_dipole_sum_1d
from cda.dipoles.dipole_2d_hex import dipole_sum_2d_hex

def test_units_and_shapes():
    lda = np.array([500e-9])
    w_ev = lda_to_ev(lda)
    k = k_from_lda(lda)
    assert w_ev.shape == (1,)
    assert k.shape == (1,)

def test_1d_sum_small():
    k = k_from_lda(np.array([500e-9]))
    S = compute_dipole_sum_1d(k, 500e-9, N=11)
    assert S.shape == (1,)
    assert np.isfinite(S[0])

def test_2d_hex_small():
    k = k_from_lda(np.array([500e-9]))
    S = dipole_sum_2d_hex(k, 500e-9, Nx=11, Ny=11)
    assert S.shape == (1,)
    assert np.isfinite(S[0])
