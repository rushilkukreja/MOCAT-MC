"""
    -----------------------------------------------------------------
    
                              Ex3_4.py
    
  this file demonstrates example 3-4.
    
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

from jday import jday

def ex3_4():
    # -------- jday         - find julian date
    year = 1996
    mon = 10
    day = 26
    hr = 14
    min_val = 20
    sec = 0.00
    print('\n--------jday test')
    print(f'year {year:4d}', end='')
    print(f'mon {mon:4d}', end='')
    print(f'day {day:3d}', end='')
    print(f'hr {hr:3d}:{min_val:2d}:{sec:8.6f}')
    
    jdut1 = jday(year, mon, day, hr, min_val, sec)
    
    print(f'jd {jdut1:18.10f}')

if __name__ == "__main__":
    ex3_4() 