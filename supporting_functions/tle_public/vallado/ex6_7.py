"""
    -----------------------------------------------------------------
    
                              ex6_7.py
    
  this file demonstrates example 6-7.
    
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
# from combined import combined  # Placeholder for actual function

def ex6_7():
    rad = 180.0 / pi
    re = 6378.137
    print('-------------------- problem ex 6-7')
    rinit = (re + 191.0) / re
    rfinal = (re + 35780.0) / re
    einit = 0.0
    efinal = 0.0
    iinit = 28.5 / rad
    ifinal = 0.0 / rad
    deltai = ifinal - iinit

    # deltai1, deltava, deltavb, gam1, gam2 = combined(rinit, rfinal, einit, efinal, deltai)
    deltai1, deltava, deltavb, gam1, gam2 = 0, 0, 0, 0, 0  # Placeholders

    print('combined maneuver')
    print(f' deltava  {deltava:11.7f}')
    print(f' deltavb  {deltavb:11.7f}')
    print(f' deltai1  {deltai1 * rad:11.7f}')
    print(f' gam1  {gam1 * rad:11.7f}')
    print(f' gam2  {gam2 * rad:11.7f}')

if __name__ == "__main__":
    ex6_7() 