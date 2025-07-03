"""
    -----------------------------------------------------------------
    
                              Ex3_8.py
    
  this file demonstrates example 3-8.
    
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

from dms2rad import dms2rad
from rad2dms import rad2dms

def ex3_8():
    # -------- dms test
    deg = -35
    min_val = -15
    sec = -53.63
    print(f'deg {deg:4d} ', end='')
    print(f'min {min_val:4d} ', end='')
    print(f'sec {sec:8.6f}')

    dms = dms2rad(deg, min_val, sec)
    print(f'dms {dms:11.7f}')

    deg2, min2, sec2 = rad2dms(dms)
    print(f' deg min sec {deg2:4d}  {min2:4d}  {sec2:8.6f}')

if __name__ == "__main__":
    ex3_8() 