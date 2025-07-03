"""
    -----------------------------------------------------------------
    
                              ex5_4.py
    
  this file demonstrates example 5-4.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
            22 jan 11  david vallado
                         original
  changes :
            22 jan 11  david vallado
                         original baseline
    
     *****************************************************************
"""

from constmath import *
from jday import jday
from moonrise1 import moonrise1
from moonrise import moonrise
from rad2hms import rad2hms

def ex5_4():
    # --------  moon         - moon rise set
    jd = jday(1998, 8, 21, 0, 0, 0.00)
    latgd = 40.0 / rad
    lon = 0.00 / rad

    utmoonrise, utmoonset, moonphaseang, error = moonrise1(jd, latgd, lon, 'y')
    print(f'moon moonrise {utmoonrise:14.4f}    moonset {utmoonset:14.4f} hrs')
    print(f'moon phase angle {moonphaseang:14.4f}')

    jd = jday(1990, 3, 5, 0, 0, 0.00)
    latgd = 40.94 / rad
    lon = -73.97 / rad

    utmoonrise, utmoonset, moonphaseang, error = moonrise1(jd, latgd, lon, 'y')
    print(f'moon moonrise {utmoonrise:14.4f}  {(utmoonrise-int(utmoonrise))*60:14.4f}   moonset {utmoonset:14.4f} {(utmoonset-int(utmoonset))*60:14.4f}')
    print(f'moon phase angle {moonphaseang:14.4f}')

    print('     40    42    44    46    48    50    52    54    56    58    60    62    64    66')
    for i in range(8, 31):
        jd = jday(2006, 6, i, 0, 0, 0.00)
        for j in range(0, 14):
            latgd = (40.0 + j * 2.0) / rad
            lon = 0.00 / rad
            utmoonrise, utmoonset, moonphaseang, error = moonrise(jd, latgd, lon, 'n')
            hr, minv, sec = rad2hms(utmoonrise * 15.0 * pi / 180.0)
            if j == 0:
                print(f'{i:2d} {hr:2d}:{minv:2d} ', end='')
            else:
                if hr == 38197:
                    print(' none ', end='')
                else:
                    if utmoonrise > 9999.0:
                        print(' nors ', end='')
                    else:
                        if utmoonrise < 0.0:
                            print(' nost ', end='')
                        else:
                            print(f'{hr:2d}:{minv:2d} ', end='')
        print()

if __name__ == "__main__":
    ex5_4() 