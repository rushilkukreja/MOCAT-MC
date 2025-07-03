"""
    -----------------------------------------------------------------
    
                              Ex1_1.py
    
  this file demonstrates example 1-1.
    
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

import numpy as np
from constmath import *
from constastro import *

def ex1_1():
    print('\n-------- ex 1-1 ---------')
    
    periodsid = 86164.090518
    # periodsid = 86400/1.002737909350795
    
    a = (mu * (periodsid / twopi) ** 2) ** (1.0 / 3.0)
    
    print(f'a {a:16.8f} {a/re:18.10f} km')

if __name__ == "__main__":
    ex1_1() 