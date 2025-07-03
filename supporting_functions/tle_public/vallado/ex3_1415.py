"""
    -----------------------------------------------------------------
    
                              ex3_1415.py
    
  this file tests the reduction functions.
    
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
# from constmath import *
# from constastro import *
# Placeholders for all the reduction and transformation functions

def ex3_1415():
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
    opt = 'a'

    print('test program for reduction functions\n')
    print('input data\n')
    print(f' year {year:5d}  mon {mon:4d}  day {day:3d}  {hr:3d}:{minv:2d}:{sec:8.6f}')
    print(f' dut1 {dut1:8.6f} s dat {dat:3d} s xp {xp:8.6f} " yp {yp:8.6f} " lod {lod:8.6f} s')
    print(f' ddpsi {ddpsi:8.6f} " ddeps  {ddeps:8.6f}')
    print(f' order {order:3d}  eqeterms {eqeterms:3d}  opt {opt:3s}')
    print('units are km and km/s and km/s2')

    # ddpsi = ddpsi * np.pi / (180 * 3600)
    # ddeps = ddeps * np.pi / (180 * 3600)
    # timezone = 0

    # The following are placeholders for the actual function calls and outputs
    print('convtime results')
    print('... (placeholder for convtime output)')
    print('precession matrix')
    print('... (placeholder for precess output)')
    print('nutation matrix')
    print('... (placeholder for nutation output)')
    print('sidereal time matrix')
    print('... (placeholder for sidereal output)')
    print('polar motion matrix')
    print('... (placeholder for polarm output)')
    print('truemean matrix')
    print('... (placeholder for truemean output)')
    print('\n\n ============== convert various coordinate systems from ecef =================== ')
    print(f'ITRF          IAU-76/FK5   {recef[0]:14.7f} {recef[1]:14.7f} {recef[2]:14.7f} v {vecef[0]:14.9f} {vecef[1]:14.9f} {vecef[2]:14.9f} a {aecef[0]:14.9f} {aecef[1]:14.9f} {aecef[2]:14.9f}')
    print('... (placeholder for ecef2pef, ecef2tod, ecef2mod, ecef2eci, eci2ecef, teme2ecef, etc.)')

if __name__ == "__main__":
    ex3_1415() 