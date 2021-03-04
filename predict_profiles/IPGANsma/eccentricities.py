import numpy as np
import cmath

def calc_ecc(e, dx, dy):
    
    r_pow = 2.
    
    N_x=e.shape[0] # number of points in x
    N_y=e.shape[1] # number of points in y
    
    n_harmonic = 5
    eps = np.zeros((n_harmonic))
    
    def r_func(ix, iy, dx, dy):
        x=dx*(2.*ix-N_x)/2.
        y=dy*(2.*iy-N_y)/2.
        r = np.sqrt(x*x + y*y)
        return r**r_pow
    
    def phi_func(ix, iy, dx, dy, n):
        x=dx*(2.*ix-N_x)/2.
        y=dy*(2.*iy-N_y)/2.
        phi = np.arctan2(y, x)
        real = np.cos(n*phi)
        imag = np.sin(n*phi)
        z = complex(real, imag)
        return z
    
    
    r_mat = np.array([[ r_func(ix, iy, dx, dy) for iy in range(N_y) ] for ix in range(N_x) ])
    
    for n in range(n_harmonic):
        phi_mat = np.array([[ phi_func(ix, iy, dx, dy, n) for iy in range(N_y) ] for ix in range(N_x) ])
        eps[n] = np.abs( np.sum( e * phi_mat * r_mat ) )

    eps = eps * dx * dy
    eps = eps / eps[0]
    
    return eps

if __name__ == '__main__':
    calc_ecc()
