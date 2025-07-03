"""
    -----------------------------------------------------------------
    
                              Ex3_6.py
    
  this file demonstrates example 3-6.
    
                          companion code for
             fundamentals of astrodyanmics and applications
                                 2007
                            by david vallado
    
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
from jday import jday
from gstime0 import gstime0
from lstime import lstime

def ex3_6():
    # -------- gstime       - greenwich sidereal time
    year = 1992
    mon = 8
    day = 20
    hr = 12
    min_val = 14
    sec = 0.00
    jdut1 = jday(year, mon, day, hr, min_val, sec)
    print(f'input jd = {jdut1:16.8f}')

    print('\n--------gstime0 test')
    print(f'input year {year:4d}')
    gst0 = gstime0(year)
    print(f'gst0 = {gst0*rad:14.8f} deg')

    # -------- lstime       - local sidereal time
    lon = -104.000 / rad
    print(f'input lon = {lon*rad:11.7f}', end='')
    lst, gst = lstime(lon, jdut1)
    print(f'gst = {gst*rad:14.8f}')
    print(f'lst {lst*rad:11.7f} gst {gst*rad:11.7f} deg')

if __name__ == "__main__":
    ex3_6() 