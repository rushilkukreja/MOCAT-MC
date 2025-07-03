"""
    -----------------------------------------------------------------
    
                              Ex3_1.py
    
  this file demonstrates example 3-1.
    
                          companion code for
             fundamentals of astrodyanmics and applications
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

def ex3_1():
    re = 6378.1363
    rad = 180.0 / np.pi
    flat = 1.0 / 298.257223563
    eccearth = np.sqrt(2.0 * flat - flat ** 2)
    eccearthsqrd = eccearth ** 2
    
    # -------------------------  implementation   -----------------
    latgd = 39.586667 / rad
    lon = -105.640 / rad
    alt = 4.347667  # km
    sinlat = np.sin(latgd)
    
    # ------  find rdel and rk components of site vector  ---------
    cearth = re / np.sqrt(1.0 - (eccearthsqrd * sinlat * sinlat))
    rdel = (cearth + alt) * np.cos(latgd)
    rk = ((1.0 - eccearthsqrd) * cearth + alt) * sinlat
    
    print(f'rdelta {rdel:16.8f} rk {rk:11.8f} km')

if __name__ == "__main__":
    ex3_1() 