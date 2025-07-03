"""
    -----------------------------------------------------------------
    
                              ex7_5.py
    
  this file demonstrates example 7-5.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (w) 719-573-2600, email dvallado@agi.com
    
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
from constmath import *
# Placeholder imports for functions to be implemented
# from lambertu import lambertu
# from lambertb import lambertb

def ex7_5():
    fid = 1
    print('\n-------- lambertu test book pg 467')
    ro = np.array([2.5, 0.0, 0.0]) * 6378.137
    r = np.array([1.9151111, 1.6069690, 0.0]) * 6378.137
    dtsec = 76.0 * 60.0
    dm = 's'
    overrev = 0
    print(f' ro {ro[0]:16.8f}{ro[1]:16.8f}{ro[2]:16.8f}')
    print(f' r  {r[0]:16.8f}{r[1]:16.8f}{r[2]:16.8f}')
    # vo, v, errorl = lambertu(ro, r, dm, overrev, dtsec, fid)
    vo, v, errorl = np.zeros(3), np.zeros(3), 0  # Placeholder
    print(f' vo {vo[0]:16.8f}{vo[1]:16.8f}{vo[2]:16.8f}')
    print(f' v  {v[0]:16.8f}{v[1]:16.8f}{v[2]:16.8f}')

    print('\n-------- lambertb test book pg 467')
    ro = np.array([2.5, 0.0, 0.0]) * 6378.137
    r = np.array([1.9151111, 1.6069690, 0.0]) * 6378.137
    dtsec = 76.0 * 60.0
    dm = 's'
    overrev = 0
    print(f' ro {ro[0]:16.8f}{ro[1]:16.8f}{ro[2]:16.8f}')
    print(f' r  {r[0]:16.8f}{r[1]:16.8f}{r[2]:16.8f}')
    # vo, v, errorl = lambertb(ro, r, dm, overrev, dtsec)
    vo, v, errorl = np.zeros(3), np.zeros(3), 0  # Placeholder
    print(f' vo {vo[0]:16.8f}{vo[1]:16.8f}{vo[2]:16.8f}')
    print(f' v  {v[0]:16.8f}{v[1]:16.8f}{v[2]:16.8f}')

    print('\n-------- lambertb test ben joseph')
    ro = np.array([6822.88933, -5147.86167, -454.39488])
    r = np.array([-4960.67860, 10585.2504, 927.1937739])
    dtsec = 4976.002
    dm = 's'
    overrev = 0
    print(f' ro {ro[0]:16.8f}{ro[1]:16.8f}{ro[2]:16.8f}')
    print(f' r  {r[0]:16.8f}{r[1]:16.8f}{r[2]:16.8f}')
    # vo, v, errorl = lambertb(ro, r, dm, overrev, dtsec)
    vo, v, errorl = np.zeros(3), np.zeros(3), 0  # Placeholder
    print(f' vo {vo[0]:16.8f}{vo[1]:16.8f}{vo[2]:16.8f}')
    print(f' v  {v[0]:16.8f}{v[1]:16.8f}{v[2]:16.8f}')

if __name__ == "__main__":
    ex7_5() 