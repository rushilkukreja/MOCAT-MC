"""
    -----------------------------------------------------------------
    
                              ex3_1415a.py
    
  this file demonstrates example 3-1415a - just the teme to ecef conversion
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (h)               email dvallado@msn.com
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
            10 dec 07  david vallado
                         original
  changes :
            10 dec 07  david vallado
                         original baseline
    
     *****************************************************************
"""

import numpy as np
# from constastro import *
# Placeholders for all the reduction and transformation functions

def ex3_1415a():
    recef = np.array([-1033.4793830, 7901.2952754, 6380.3565958])
    vecef = np.array([-3.225636520, -2.872451450, 5.531924446])
    aecef = np.array([0.001, 0.002, 0.003])

    year = 2004
    mon = 4
    day = 6
    hr = 7
    minv = 51
    sec = 28.386009
    dut1 = -0.4399619
    dat = 32
    xp = -0.140682
    yp = 0.333309
    lod = 0.0015563
    ddpsi = -0.052195
    ddeps = -0.003875
    timezone = 0
    order = 106
    eqeterms = 2

    print('teme to ecef conversion example')
    print(f' ecef {recef[0]:14.7f}{recef[1]:14.7f}{recef[2]:14.7f} v {vecef[0]:14.9f}{vecef[1]:14.9f}{vecef[2]:14.9f} a {aecef[0]:14.9f}{aecef[1]:14.9f}{aecef[2]:14.9f}')
    print('... (placeholder for ecef2teme, teme2ecef, etc.)')
    print('... (placeholder for sgp4 example and further conversions)')

if __name__ == "__main__":
    ex3_1415a() 