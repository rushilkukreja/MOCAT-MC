"""
    -----------------------------------------------------------------
    
                              Ex3_7.py
    
  this file demonstrates example 3-7.
    
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

from convtime import convtime

def ex3_7():
    year = 2004
    mon = 5
    day = 14
    hr = 10
    min_val = 43
    sec = 0.0
    dut1 = -0.463326
    dat = 32
    xp = 0.0
    yp = 0.0
    lod = 0.0
    timezone = 6

    # -------- convtime    - convert time from utc to all the others
    ut1, tut1, jdut1, utc, tai, tt, ttt, jdtt, tdb, ttdb, jdtdb = convtime(
        year, mon, day, hr, min_val, sec, timezone, dut1, dat)

    print(f'ut1 {ut1:8.6f} tut1 {tut1:16.12f} jdut1 {jdut1:18.11f}')
    print(f'utc {utc:8.6f}')
    print(f'tai {tai:8.6f}')
    print(f'tt  {tt:8.6f} ttt  {ttt:16.12f} jdtt  {jdtt:18.11f}')
    print(f'tdb {tdb:8.6f} ttdb {ttdb:16.12f} jdtdb {jdtdb:18.11f}')

if __name__ == "__main__":
    ex3_7() 