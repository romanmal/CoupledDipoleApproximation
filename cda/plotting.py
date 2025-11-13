import matplotlib.pyplot as plt

def plot_qext(wavelengths_nm, qext, label=None, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8,4.5))
    ax.plot(wavelengths_nm, qext, label=label)
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Q_ext")
    if label:
        ax.legend()
    return ax

def plot_lattice_peaks(lat_nm, peak_nm, ax=None):
    if ax is None:
        fig, ax = plt.subplots()
    ax.plot(lat_nm, peak_nm, marker='o')
    ax.plot(lat_nm, lat_nm, 'r--', label='y=x')
    ax.set_xlabel('Lattice const (nm)')
    ax.set_ylabel('Lattice peak location (nm)')
    ax.legend()
    return ax
