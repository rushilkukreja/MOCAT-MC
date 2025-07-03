"""
    -----------------------------------------------------------------
    
                              ex5_3.py
    
  this file demonstrates example 5-3.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
             7 jun 07  david vallado
                         original
  changes :
            13 feb 07  david vallado
                         original baseline
    
     *****************************************************************
"""

from constmath import *
from moon import moon

def ex5_3():
    # --------  moon         - analytical moon ephemeris
    jd = 2449470.5
    rmoon, rtasc, decl = moon(jd)
    print(f'moon rtasc {rtasc*rad:14.4f} deg decl {decl*rad:14.4f} deg')
    print(f'moon {rmoon[0]:14.7f}{rmoon[1]:14.7f}{rmoon[2]:14.7f} er')
    print(f'moon {rmoon[0]*6378.137:14.4f}{rmoon[1]*6378.137:14.4f}{rmoon[2]*6378.137:14.4f} km')

if __name__ == "__main__":
    ex5_3() 