"""
    -----------------------------------------------------------------
    
                              ex5_6.py
    
  this file demonstrates example 5-6.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
            26 mar 11  david vallado
                         original
  changes :
            26 mar 11  david vallado
                         original baseline
    
     *****************************************************************
"""

from constmath import *
from jday import jday
from sight import sight
from sun import sun


def ex5_6():
    jd = jday(1995, 2, 15, 12, 0, 0.00)
    r1 = [0.0, -4464.696, -5102.509]  # km
    r2 = [0.0, 5740.323, 3189.068]

    los = sight(r1, r2, 's')
    print('los:', los)

    jd = jday(1995, 2, 15, 0, 0, 0.00)
    rsun, rtasc, decl = sun(jd)
    print(f'sun MOD {rsun[0]:11.9f}{rsun[1]:11.9f}{rsun[2]:11.9f} au')
    print(f'sun MOD {rsun[0]*149597870.0:14.4f}{rsun[1]*149597870.0:14.4f}{rsun[2]*149597870.0:14.4f} km')

    los = sight(r1, [x*149597870.0 for x in rsun], 's')
    print('los:', los)

if __name__ == "__main__":
    ex5_6() 