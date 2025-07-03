"""
    -----------------------------------------------------------------
    
                              ex6_14.py
    
  this file demonstrates example 6-14.
    
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
# from hillsr import hillsr  # Placeholder for actual function

def ex6_14():
    print('-------------------- problem ex 6-14')
    ro = np.array([0.0, 0.0, 0.0])
    vo = np.array([-0.1, -0.04, -0.02])  # m/s
    ralt = 590.0  # km
    dtsec = 0.0
    # rint, vint = hillsr(ro, vo, ralt, dtsec)
    rint, vint = np.zeros(3), np.zeros(3)  # Placeholders
    print('initial interceptor position')
    print(f' r  {rint[0]:11.7f}  {rint[1]:11.7f}  {rint[2]:11.7f}')
    print(f' v  {vint[0]:11.7f}  {vint[1]:11.7f}  {vint[2]:11.7f}\n')

    dtsec = 300.0
    # rint, vint = hillsr(ro, vo, ralt, dtsec)
    rint, vint = np.zeros(3), np.zeros(3)  # Placeholders
    print(f' r  {rint[0]:11.7f}  {rint[1]:11.7f}  {rint[2]:11.7f}')
    print(f' v  {vint[0]:11.7f}  {vint[1]:11.7f}  {vint[2]:11.7f}\n')

    dtsec = 1200.0
    # rint, vint = hillsr(ro, vo, ralt, dtsec)
    rint, vint = np.zeros(3), np.zeros(3)  # Placeholders
    print(f' r  {rint[0]:11.7f}  {rint[1]:11.7f}  {rint[2]:11.7f}')
    print(f' v  {vint[0]:11.7f}  {vint[1]:11.7f}  {vint[2]:11.7f}\n')

    dtsec = 600.0
    # rint, vint = hillsr(ro, vo, ralt, dtsec)
    rint, vint = np.zeros(3), np.zeros(3)  # Placeholders
    # No print for this last one in the original

if __name__ == "__main__":
    ex6_14() 