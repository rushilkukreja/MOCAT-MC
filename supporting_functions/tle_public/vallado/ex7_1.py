"""
    -----------------------------------------------------------------
    
                              ex7_1.py
    
  this file demonstrates example 7-1.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
             7 jun 07  david vallado
                         original
  changes :
            13 feb 07  david vallado
                         original baseline
    
     *****************************************************************
"""

import numpy as np
from constmath import *
from jday import jday
# Placeholder imports for functions to be implemented
# from site import site
# from razel2rv import razel2rv
# from rv2razel import rv2razel

def ex7_1():
    # ---- site
    print('\n-------- site test')
    latgd = 39.007 / rad
    lon = -104.883 / rad
    alt = 2.1870
    jd = jday(1995, 5, 20, 3, 17, 2.0)
    # rs, vs = site(latgd, lon, alt)
    rs, vs = [0, 0, 0], [0, 0, 0]  # Placeholder
    print(f'site {rs[0]:14.7f}{rs[1]:14.7f}{rs[2]:14.7f}{vs[0]:14.7f}{vs[1]:14.7f}{vs[2]:14.7f}')

    print('--------------- razel tests ----------------------------')
    latgd = 39.007 / rad
    lon = -104.883 / rad
    alt = 2.187
    rho = 604.68
    az = 205.6 / rad
    el = 30.7 / rad
    drho = 2.08
    daz = 0.15 / rad
    delv = 0.17 / rad
    year = 1995
    mon = 5
    day = 20
    hr = 3
    minv = 17
    sec = 2.0
    dut1 = 0.0
    dat = 29
    xp = 0.0
    yp = 0.0
    lod = 0.0
    timezone = 0
    terms = 0
    ddpsi = 0.0
    ddeps = 0.0

    utc = sec
    ut1 = utc + dut1
    tai = utc + dat
    tt = tai + 32.184
    jdut1 = jday(year, mon, day, hr, minv, ut1)
    jdtt = jday(year, mon, day, hr, minv, tt)
    ttt = (jdtt - 2451545.0) / 36525.0

    print(f'year {year:5d} mon {mon:4d} day {day:3d} hr {hr:3d}:{minv:2d}:{sec:8.6f}')
    print(f'dut1 {dut1:8.6f} s dat {dat:3d} s xp {xp:8.6f} " yp {yp:8.6f} " lod {lod:8.6f} s')
    print('           range km        az deg      el    deg     rngrt km/s      azrate deg/s  elrate deg/s')
    print(f'rvraz {rho:14.7f}{az*rad:14.7f}{el*rad:14.7f}{drho:14.7f}{daz*rad:14.7f}{delv*rad:14.7f}')

    # reci, veci = razel2rv(rho, az, el, drho, daz, delv, latgd, lon, alt, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps)
    reci, veci = [0, 0, 0], [0, 0, 0]  # Placeholder
    print(f'r    {reci[0]:14.7f}{reci[1]:14.7f}{reci[2]:14.7f} v {veci[0]:14.9f}{veci[1]:14.9f}{veci[2]:14.9f}')

    # rho, az, el, drho, daz, delv = rv2razel(reci, veci, latgd, lon, alt, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps)
    rho, az, el, drho, daz, delv = 0, 0, 0, 0, 0, 0  # Placeholder
    print(f'rvraz {rho:14.7f}{az*rad:14.7f}{el*rad:14.7f}{drho:14.7f}{daz*rad:14.7f}{delv*rad:14.7f}')

if __name__ == "__main__":
    ex7_1() 