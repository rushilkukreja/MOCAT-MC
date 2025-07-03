"""
    -----------------------------------------------------------------
    
                              ex6_8.py
    
  this file demonstrates example 6-8.
    
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
# from rendz import rendz  # Placeholder for actual function

def ex6_8():
    rad = 180.0 / pi
    re = 6378.137
    print('-------------------- problem ex 6-8')
    rcs1 = 12756.274 / re
    rcs3 = 12756.274 / re
    phasei = 20.0 / rad
    einit = 0.0
    efinal = 0.0
    nuinit = 0.0 / rad
    nufinal = 0.0 / rad
    ktgt = 1
    kint = 1

    # phasef, waittime, deltav = rendz(rcs1, rcs3, phasei, einit, efinal, nuinit, nufinal, ktgt, kint)
    phasef, waittime, deltav = 0, 0, 0  # Placeholders
    print('rendezvous')
    print(f' phasef {phasef * rad:11.7f}')
    print(f' waittime {waittime:11.7f}')
    print(f' deltav {deltav:11.7f}')

    ktgt = 2
    kint = 2
    # phasef, waittime, deltav = rendz(rcs1, rcs3, phasei, einit, efinal, nuinit, nufinal, ktgt, kint)
    phasef, waittime, deltav = 0, 0, 0  # Placeholders
    print('rendezvous')
    print(f' phasef {phasef * rad:11.7f}')
    print(f' waittime {waittime:11.7f}')
    print(f' deltav {deltav:11.7f}')

if __name__ == "__main__":
    ex6_8() 