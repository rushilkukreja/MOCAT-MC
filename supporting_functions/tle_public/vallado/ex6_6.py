"""
    -----------------------------------------------------------------
    
                              ex6_6.py
    
  this file demonstrates example 6-6.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
            25 nov 08  david vallado
                         original
  changes :
            25 nov 08  david vallado
                         original baseline
    
     *****************************************************************
"""

import numpy as np
from math import pi
# from iandnode import iandnode  # Placeholder for actual function

def ex6_6():
    rad = 180.0 / pi
    re = 6378.137
    mu = 1.0  # canonical

    print('-------------------- problem ex 6-6')
    iinit = 55.0 / rad
    ifinal = 40.0 / rad
    ecc = 0.0
    deltaomega = 45.0 / rad
    vinit = 5.892311 / 7.905365
    fpa = 0.0 / rad

    # deltav = iandnode(iinit, deltaomega, ifinal, vinit, fpa)
    deltav = 0  # Placeholder

    print('inclination and node changes')
    print(f' deltav  {deltav:11.7f}')

if __name__ == "__main__":
    ex6_6() 