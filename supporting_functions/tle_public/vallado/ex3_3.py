"""
    -----------------------------------------------------------------
    
                              Ex3_3.py
    
  this file demonstrates example 3-3.
    
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

from constmath import *
from ijk2ll import ijk2ll
from ijk2llb import ijk2llb

def ex3_3():
    # --------  ijk2ll       - position to lat lon alt almanac (fastest)
    r1 = [6524.834, 6862.875, 6448.296]
    latgc, latgd, lon, hellp = ijk2ll(r1)
    print(f'ijk2ll gc {latgc*rad:14.7f} gd {latgd*rad:14.7f} {lon*rad:14.7f}{hellp:14.7f}')

    # --------  ijk2llb      - position to lat lon alt borkowski
    latgc, latgd, lon, hellp = ijk2llb(r1)
    print(f'ijk2ll gc {latgc*rad:14.7f} gd {latgd*rad:14.7f} {lon*rad:14.7f}{hellp:14.7f}')

if __name__ == "__main__":
    ex3_3() 