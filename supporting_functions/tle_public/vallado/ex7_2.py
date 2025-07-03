"""
    -----------------------------------------------------------------
    
                              ex7_2.py
    
  this file demonstrates example 7-2.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
             9 oct 07  david vallado
                         original
  changes :
             9 oct 07  david vallado
                         original baseline
    
     *****************************************************************
"""

import numpy as np
from constmath import *
from constastro import *
from jday import jday
# Placeholder imports for functions to be implemented
# from site import site
# from invjday import invjday
# from convtime import convtime
# from ecef2eci import ecef2eci
# from anglesdr import anglesdr
# from rv2coe import rv2coe

def ex7_2():
    # gaussian angles only (vallado book, p. 420 new effort)
    jd1 = jday(2007, 8, 20, 11, 40, 0.000)
    jd2 = jday(2007, 8, 20, 11, 50, 0.000)
    jd3 = jday(2007, 8, 20, 12, 20, 0.000)  # try unequally spaced obs

    # topocentric values
    rtasc1 = -0.4172870 / rad
    rtasc2 = 55.0931551 / rad
    rtasc3 = 134.2826693 / rad
    decl1 = 17.4626616 / rad
    decl2 = 36.5731946 / rad
    decl3 = 12.0351097 / rad

    # site position
    latgd = 40.0 / rad
    lon = -110.0 / rad
    alt = 2.0  # km

    # at 8-20-07 11:50,
    r2ans = np.array([5963.6422128, 5722.1777645, 6660.2466242])
    v2ans = np.array([-4.3643202, 4.6055371, 1.5157093])
    # p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = rv2coe(r2ans, v2ans)
    p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = [0]*11  # Placeholder
    print(f'ans coes {p:11.4f}{a:11.4f}{ecc:13.9f}{incl*rad:13.7f}{omega*rad:11.5f}{argp*rad:11.5f}{nu*rad:11.5f}{m*rad:11.5f}')

    year = 2007
    mon = 8
    day = 20
    hr = 11
    minv = 50
    sec = 0.0000
    dut1 = 0.0
    dat = 33
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

    # -------------- convert each site vector from ecef to eci -----------------
    # rs, vs = site(latgd, lon, alt)  # in ecef
    rs, vs = np.zeros(3), np.zeros(3)  # Placeholder
    a = np.zeros(3)  # dummy acceleration variable for the ecef2eci routine
    # The following would be replaced with actual function calls
    rsite1, vseci, aeci = np.zeros(3), np.zeros(3), np.zeros(3)
    rsite2, vseci, aeci = np.zeros(3), np.zeros(3), np.zeros(3)
    rsite3, vseci, aeci = np.zeros(3), np.zeros(3), np.zeros(3)

    # r2, v2 = anglesdr(decl1, decl2, decl3, rtasc1, rtasc2, rtasc3, jd1, jd2, jd3, rsite1, rsite2, rsite3)
    r2, v2 = np.zeros(3), np.zeros(3)  # Placeholder

    print(f'v2     {v2[0]:11.7f}   {v2[1]:11.7f}  {v2[2]:11.7f} ')
    print(f'v2 {v2[0]/velkmps:11.7f}   {v2[1]/velkmps:11.7f}  {v2[2]/velkmps:11.7f}')
    print(f'v2 ans {v2ans[0]:11.7f}   {v2ans[1]:11.7f}  {v2ans[2]:11.7f} ')
    print(f'v2 {v2ans[0]/velkmps:11.7f}   {v2ans[1]/velkmps:11.7f}  {v2ans[2]/velkmps:11.7f}')
    print(f'r2     {r2[0]/re:11.7f}   {r2[1]/re:11.7f}  {r2[2]/re:11.7f}   {r2[0]:11.7f}  {r2[1]:11.7f}  {r2[2]:11.7f}')
    print(f'r2 ans {r2ans[0]/re:11.7f}   {r2ans[1]/re:11.7f}  {r2ans[2]/re:11.7f}   {r2ans[0]:11.7f}  {r2ans[1]:11.7f}  {r2ans[2]:11.7f}')

    # p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = rv2coe(r2, v2)
    p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = [0]*11  # Placeholder
    print('          p km       a km      ecc      incl deg     raan deg     argp deg      nu deg      m deg      arglat   truelon    lonper')
    print(f'    coes {p:11.4f}{a:11.4f}{ecc:13.9f}{incl*rad:13.7f}{omega*rad:11.5f}{argp*rad:11.5f}{nu*rad:11.5f}{m*rad:11.5f}{arglat*rad:11.5f}{truelon*rad:11.5f}{lonper*rad:11.5f}')

    # p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = rv2coe(r2ans, v2ans)
    p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = [0]*11  # Placeholder
    print(f'ans coes {p:11.4f}{a:11.4f}{ecc:13.9f}{incl*rad:13.7f}{omega*rad:11.5f}{argp*rad:11.5f}{nu*rad:11.5f}{m*rad:11.5f}')

if __name__ == "__main__":
    ex7_2() 