"""
    -----------------------------------------------------------------
    
                              Ex2_4.py
    
  this file demonstrates example 2-4.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2004
                            by david vallado
    
     (h)               email dvallado@msn.com
     (w) 719-573-2600, email dvallado@stk.com
    
     *****************************************************************
    
  current :
            30 mar 07  david vallado
                         original
  changes :
            13 feb 07  david vallado
                         original baseline
    
     *****************************************************************
"""

import numpy as np
from constastro import *
from kepler import kepler

def ex2_4():
    print('\n-------- kepler  ex 2-4, pg 102 ---------')
    
    # initial vectors in km and km/s
    ro = np.array([1131.340, -2282.343, 6672.423])
    vo = np.array([-5.64305, 4.30333, 2.42879])
    print('input:')
    print(f'ro {ro[0]:16.8f} {ro[1]:16.8f} {ro[2]:16.8f} km')
    print(f'vo {vo[0]:16.8f} {vo[1]:16.8f} {vo[2]:16.8f} km/s')
    
    # convert 40 minutes to seconds
    dtsec = 40.0 * 60.0
    print(f'dt {dtsec:16.8f} sec')
    print('intermediate values:')
    
    r1, v1 = kepler(ro, vo, dtsec)
    
    # answer in km and km/s
    print('output:')
    print(f'r1 {r1[0]/re:16.8f} {r1[1]/re:16.8f} {r1[2]/re:16.8f} er')
    print(f'r1 {r1[0]:16.8f} {r1[1]:16.8f} {r1[2]:16.8f} km')
    print(f'v1 {v1[0]/velkmps:16.8f} {v1[1]/velkmps:16.8f} {v1[2]/velkmps:16.8f} er/tu')
    print(f'v1 {v1[0]:16.8f} {v1[1]:16.8f} {v1[2]:16.8f} km/s')

if __name__ == "__main__":
    ex2_4() 