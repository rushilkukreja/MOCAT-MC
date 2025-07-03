"""
    -----------------------------------------------------------------
    
                              Ex2_2.py
    
  this file demonstrates example 2-2.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (h)               email dvallado@msn.com
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
            30 mar 07  david vallado
                         original
  changes :
            13 feb 07  david vallado
                         original baseline
    
     *****************************************************************
"""

from constmath import *
from newtone import newtone
from newtonm import newtonm
from newtonnu import newtonnu

def ex2_2():
    # --------  newtone      - find true and mean anomaly given ecc and eccentric anomaly
    ecc = 0.4
    e0 = 334.566986 / rad
    print('              m             nu           e           e0')
    m, nu = newtone(ecc, e0)
    print(f'newe  {m*rad:14.4f}{nu*rad:14.4f}{ecc:14.4f}{e0*rad:14.7f}')

    # --------  newtonm      - find eccentric and true anomaly given ecc and mean anomaly
    ecc = 0.34
    m = 235.4 / rad
    print('             e0             nu           e           m')
    e0, nu = newtonm(ecc, m)
    print(f'newm  {e0*rad:14.4f}{nu*rad:14.4f}{ecc:14.4f}{m*rad:14.7f}')

    # --------  newtonnu     - find eccentric and mean anomaly given ecc and true anomaly
    ecc = 0.34
    nu = 134.567001 / rad
    print('             e0             m            e           nu')
    e0, m = newtonnu(ecc, nu)
    print(f'newnu {e0*rad:14.4f}{m*rad:14.4f}{ecc:14.4f}{nu*rad:14.7f}')

if __name__ == "__main__":
    ex2_2() 