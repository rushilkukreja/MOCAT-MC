"""
    -----------------------------------------------------------------
    
                              Ex3_2.py
    
  this file demonstrates example 3-2.
    
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
from constastro import *
from constmath import *
from dms2rad import dms2rad
from mag import mag
from gd2gc import gd2gc

def ex3_2():
    deg = -7
    min_val = -54
    sec = -23.886
    print(f'deg {deg:2d} min {min_val:2d} sec {sec:8.6f}')
    latgd = dms2rad(deg, min_val, sec)
    print(f'dms = {latgd*rad:11.7f} rad')
    
    deg = 345
    min_val = 35
    sec = 51.000
    print(f'deg {deg:2d} min {min_val:2d} sec {sec:8.6f}')
    lon = dms2rad(deg, min_val, sec)
    print(f'dms = {lon*rad:11.7f} rad')
    
    alt = 0.056
    
    # -------------------------  implementation   -----------------
    sinlat = np.sin(latgd)
    earthrate = np.array([0.0, 0.0, omegaearth])
    
    # ------  find rdel and rk components of site vector  ---------
    cearth = re / np.sqrt(1.0 - (eccearthsqrd * sinlat * sinlat))
    rdel = (cearth + alt) * np.cos(latgd)
    rk = ((1.0 - eccearthsqrd) * cearth + alt) * sinlat
    
    # (1.0-eccearthsqrd)*cearth
    
    # ---------------  find site position vector  -----------------
    rs = np.array([rdel * np.cos(lon), rdel * np.sin(lon), rk])
    
    print(f'site gd {rs[0]:16.9f} {rs[1]:16.9f} {rs[2]:16.9f}')
    
    rsmag = mag(rs)
    
    latgc = gd2gc(latgd)
    
    r = np.array([rsmag * np.cos(latgc) * np.cos(lon), 
                  rsmag * np.cos(latgc) * np.sin(lon), 
                  rsmag * np.sin(latgc)])
    
    print(f'site gc {r[0]:16.9f} {r[1]:16.9f} {r[2]:16.9f}')

if __name__ == "__main__":
    ex3_2() 