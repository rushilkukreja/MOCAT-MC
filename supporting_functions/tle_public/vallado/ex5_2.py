"""
    -----------------------------------------------------------------
    
                              ex5_2.py
    
  this file demonstrates example 5-2 and 5-4 for sun and moon rise/set.
    
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
from jday import jday
from sunriset import sunriset

def ex5_2():
    # --------  sun         - sun rise set
    jd = jday(1996, 3, 23, 0, 0, 0.00)
    latgd = 40.0 / rad
    lon = 0.00 / rad
    whichkind = 's'

    utsunrise, utsunset, error = sunriset(jd, latgd, lon, whichkind)
    print(f'sun sunrise {utsunrise:14.4f}  {(utsunrise - int(utsunrise))*60:14.4f}  sunset {utsunset:14.4f} {(utsunset - int(utsunset))*60:14.4f}')

    jd = jday(2011, 6, 25, 0, 0, 0.00)
    latgd = 40.9 / rad
    lon = -74.3 / rad
    whichkind = 's'

    utsunrise, utsunset, error = sunriset(jd, latgd, lon, whichkind)
    print(f'sun sunrise {utsunrise:14.4f}  {(utsunrise - int(utsunrise))*60:14.4f}  sunset {utsunset:14.4f} {(utsunset - int(utsunset))*60:14.4f}')

if __name__ == "__main__":
    ex5_2() 