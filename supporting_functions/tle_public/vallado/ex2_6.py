"""
    -----------------------------------------------------------------
    
                              Ex2_6.py
    
  this file demonstrates example 2-6.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (h)               email dvallado@msn.com
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
            13 feb 07  david vallado
                         original
  changes :
            13 feb 07  david vallado
                         original baseline
    
     *****************************************************************
"""

import numpy as np
from constmath import *
from constastro import *
from coe2rv import coe2rv

def ex2_6():
    print('coe test ----------------------------')
    p = 11067.790  # km
    ecc = 0.83285
    incl = 87.87 / rad
    omega = 227.89 / rad
    argp = 53.38 / rad
    nu = 92.335 / rad
    arglat = 0.0
    truelon = 0.0
    lonper = 0.0
    
    a = p / (1 - ecc * ecc)
    
    print('          p km       a km      ecc      incl deg     raan deg     argp deg      nu deg      m deg      arglat   truelon    lonper')
    print(f'coes {p:11.4f} {a:11.4f} {ecc:13.9f} {incl*rad:13.7f} {omega*rad:11.5f} {argp*rad:11.5f} {nu*rad:11.5f} {arglat*rad:11.5f} {truelon*rad:11.5f} {lonper*rad:11.5f}')
    
    # --------  coe2rv       - classical elements to position and velocity
    r, v = coe2rv(p, ecc, incl, omega, argp, nu, arglat, truelon, lonper)
    print(f'r    {r[0]:15.9f} {r[1]:15.9f} {r[2]:15.9f}', end='')
    print(f' v {v[0]:15.10f} {v[1]:15.10f} {v[2]:15.10f}')

if __name__ == "__main__":
    ex2_6() 