"""
    -----------------------------------------------------------------
    
                              ex3_5.py
    
  this file demonstrates example 3-5.
    
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
from constmath import *
from jday import jday
# from lstime import lstime  # Placeholder for actual function

def ex3_5():
    # -------- gstime       - greenwich sidereal time
    year = 1992
    mon = 8
    day = 20
    hr = 12
    minv = 14
    sec = 0.00
    jdut1 = jday(year, mon, day, hr, minv, sec)
    print(f'input jd = {jdut1:16.8f}')

    tut1 = (jdut1 - 2451545.0) / 36525.0
    print(f'tut1 = {tut1}')

    temp = -6.2e-6 * tut1**3 + 0.093104 * tut1**2 + (876600.0 * 3600.0 + 8640184.812866) * tut1 + 67310.54841
    # 360/86400 = 1/240, to deg, to rad
    # temp = np.remainder(temp * rad / 240.0, twopi)
    temp = np.remainder(temp, 86400)
    temp = temp / 240.0
    if temp < 0.0:
        temp = temp + 360
    gst = temp
    print(f'gst = {gst:16.12f}')

    # -------- lstime       - local sidereal time
    lon = -104.000 / rad
    print(f'input lon = {lon*rad:11.7f}')
    # lst, gst = lstime(lon, jdut1)
    lst = 0  # Placeholder
    print(f'lst {lst*rad:14.10f} gst {gst*rad:14.10f} deg')

if __name__ == "__main__":
    ex3_5() 