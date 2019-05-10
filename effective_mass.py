import numpy as np
from scipy import constants
from scipy.interpolate import CubicSpline
from scipy.misc import derivative

# parameteres set by user
bands_data_file = "results-nonrel/phosphorene.bands.dat.gnu" 
num_kpoint_x = 20   # according to Quantum Espresso Input file
num_kpoint_y = 20   # according to Quantum Espresso Input file
which_band = 11     # conduction band is the eleventh band
lattice_a = 4.447   # in Angstrom
lattice_b = 3.362   # in Angstrom
    
def effectiveMass(file=bands_data_file, target_band=which_band, num_x=num_kpoint_x, num_y=num_kpoint_y, a=lattice_a, b=lattice_b):
    # get the energies of target_band
    band_data = np.loadtxt(file) 
    k_vals = np.unique(band_data[:,0])
    num_bands = len(band_data[band_data[:,0] == k_vals[0]])
    num_k = len(k_vals)
    bands = []
    for i in range(0, num_bands):
        bands.append(np.zeros([num_k, 2])) 
    for i in range(0, num_k):
        eigen_energies = band_data[band_data[:,0] == k_vals[i]]  
        for j in range(0, num_bands):
            bands[j][i][0] = k_vals[i]
            bands[j][i][1] = np.multiply(eigen_energies[j][1], 1.0)
    energy_vals = bands[target_band - 1][:, 1] 
    # change units to atomic 
    a0 = constants.physical_constants["Bohr radius"][0]*1.0e10 # in Angstrom 
    Ry = constants.physical_constants["Rydberg constant times hc in eV"][0] # in eV
    a = a/a0
    b = b/a0
    energy_vals = energy_vals/Ry
    # unidirectional bands 
    k_x = np.linspace(-0.5, 0.5, num=2*num_x + 1, endpoint=True)*(2.0*np.pi/a)
    k_y = np.linspace(-0.5, 0.5, num=2*num_y + 1, endpoint=True)*(2.0*np.pi/b)
    energy_y = np.concatenate((energy_vals[0:num_kpoint_y], energy_vals[num_kpoint_y::-1]), axis=0)
    energy_f = energy_vals[::-1]
    energy_x = np.concatenate((energy_f[0:num_kpoint_x], energy_f[num_kpoint_x::-1]), axis=0)
    # interpolation 
    f_x = CubicSpline(k_x, energy_x) 
    f_y = CubicSpline(k_y, energy_y) 
    # calculate effective mass at k=0
    m_x = 2.0/derivative(f_x, 0.0, dx=1.0e-6, n=2)
    m_y = 2.0/derivative(f_y, 0.0, dx=1.0e-6, n=2)
    return m_x, m_y
    
print(effectiveMass())