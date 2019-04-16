import numpy as np 
from scipy import constants
from numpy import linalg as la

# default parameters
# bulk (Takao's paper) 
a_ = 4.376
b_ = 3.314 
d1_ = 2.224
d2_ = 2.244
alpha1_ = 96.34
alpha2_ = 102.09

def get_beta(a = a_, d1 = d1_, d2 = d2_ , alpha1 = alpha1_):
        alpha1 = alpha1/180.0*np.pi
        return np.arcsin((a - 2.0*d1*np.cos(alpha1/2.0))/(2.0*d2))

def alpha2(a = a_, d1 = d1_, d2 = d2_, alpha1 = alpha1_):
        beta = get_beta(a, d1, d2, alpha1)
        alpha1 = alpha1/180.0*np.pi
        # distance between atoms on different ends of d1 and d2
        d = np.sqrt((d1*np.cos(alpha1/2.0) - d2*np.sin(beta))**2 + (d1*np.sin(alpha1/2.0))**2 + (d2*np.cos(beta))**2) 
        # calculate alpha2 using cosine rule 
        alpha2 = np.arccos((d**2 - d1**2 - d2**2)/(2.0*d1*d2))
        print("beta = %5.2f " % (beta/np.pi*180))
        print("alpha2 = %5.2f " % (alpha2/np.pi*180))

def geometrical_to_cartesian(a = a_, b = b_, d1 = d1_, d2 = d2_, alpha = alpha1_, beta = get_beta(a_, d1_, d2_, alpha1_)/np.pi*180.0):
    # convert degree to radian 
    alpha = alpha/180*np.pi
    beta = beta/180*np.pi
    # calculate positions of 4 atoms 
    x1 = -0.5*d2*np.sin(beta)
    y1 = 0.0 
    z1 = 0.5*d2*np.cos(beta)
    x3 = x1 - d1*np.cos(alpha/2.0) 
    y3 = d1*np.sin(alpha/2.0)
    z3 = z1
    x2 = -x1 
    y2 = -y1 
    z2 = -z1 
    x4 = -x3 
    y4 = -y3  
    z4 = -z3
    # Bohr radius in Angstrom
    bohr = constants.physical_constants["Bohr radius"][0]*1.0e10
    cell_dim_1 = a/bohr
    cell_dim_2 = b/a
    print("celldm(1) = %5.3f\ncelldm(2) = %5.3f" % (cell_dim_1, cell_dim_2))
    print("P %5.3f %5.3f %5.3f" % (x1/bohr, y1/bohr, z1/bohr))
    print("P %5.3f %5.3f %5.3f" % (x2/bohr, y2/bohr, z2/bohr))
    print("P %5.3f %5.3f %5.3f" % (x3/bohr, y3/bohr, z3/bohr))
    print("P %5.3f %5.3f %5.3f" % (x4/bohr, y4/bohr, z4/bohr))

def cartesian_to_geometrical(cell_dim_1 = 8.269, cell_dim_2 = 0.757, 
        x=np.array([[-0.666, 0.000, 2.013], 
                [0.666, -0.000, -2.013], 
                [-3.469, 3.132, 2.013], 
                [3.469, -3.132, -2.013]])):
    d1 = la.norm(x[0, :] - x[2, :])
    d2 = la.norm(x[0, :] - x[1, :])
    # Bohr radius in Angstrom
    bohr = constants.physical_constants["Bohr radius"][0]*1.0e10
    # convert to Angstrom 
    d1 = d1*bohr
    d2 = d2*bohr
    # calculate lattice parameters 
    a = cell_dim_1*bohr
    b = cell_dim_2*a
    # calculate angles 
    alpha = 2.0*np.arcsin(b/(2.0*d1))
    beta = np.arcsin((a - 2.0*d1*np.cos(alpha/2.0))/(2.0*d2))
    # convert radian to degree 
    alpha = alpha/np.pi*180
    beta = beta/np.pi*180
    print("a = %5.3f, b = %5.3f, d1 = %5.3f, d2 = %5.3f, alpha = %5.2f, beta = %5.2f" % (a, b, d1, d2, alpha, beta))

alpha2()
geometrical_to_cartesian()
cartesian_to_geometrical()