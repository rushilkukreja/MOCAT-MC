"""
    -----------------------------------------------------------------
    
                              Ex3_9.py
    
  this file demonstrates example 3-9.
    
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

from hms2rad import hms2rad
from rad2hms import rad2hms

def ex3_9():
    # -------- hms test
    deg = 15
    min_val = 15
    sec = 53.63
    print(f'deg {deg:4d} ', end='')
    print(f'min {min_val:4d} ', end='')
    print(f'sec {sec:8.6f} ')

    hms = hms2rad(deg, min_val, sec)
    print(f'hms {hms:11.7f}')

    hr, min2, sec2 = rad2hms(hms)
    print(f' hr min sec {hr:4d}  {min2:4d}  {sec2:8.6f}')

if __name__ == "__main__":
    ex3_9() 