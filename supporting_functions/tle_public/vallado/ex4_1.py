"""
    -----------------------------------------------------------------
    
                              Ex4_1.py
    
  this file demonstrates example 4-1.
    
                          companion code for
             fundamentals of astrodyanmics and applications
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
from convtime import convtime
from lstime import lstime
from radec2rv import radec2rv
from rv2radec import rv2radec
from razel2rv import razel2rv
from rv2razel import rv2razel
from rv2ell import rv2ell
from ell2rv import ell2rv
from rv2tradc import rv2tradc
# from tradc2rv import tradc2rv  # Placeholder, if implemented

def ex4_1():
    print('--------------- book angle conversion tests ----------------------------')
    latgd = 39.007 / rad
    lon = -104.883 / rad
    alt = 2.19456  # km

    year = 1994
    mon = 5
    day = 14
    hr = 13
    min_val = 11
    sec = 20.59856

    dut1 = 0.0
    dat = 32
    xp = 0.0
    yp = 0.0
    lod = 0.0
    timezone = 0
    order = 106
    terms = 2

    ut1, tut1, jdut1, utc, tai, tt, ttt, jdtt, tdb, ttdb, jdtdb = convtime(
        year, mon, day, hr, min_val, sec, timezone, dut1, dat)
    print(f'ut1 {ut1:8.6f} tut1 {tut1:16.12f} jdut1 {jdut1:18.11f}')
    print(f'utc {utc:8.6f}')
    print(f'tai {tai:8.6f}')
    print(f'tt  {tt:8.6f} ttt  {ttt:16.12f} jdtt  {jdtt:18.11f}')
    print(f'tdb {tdb:8.6f} ttdb {ttdb:16.12f} jdtdb {jdtdb:18.11f}')

    lst, gst = lstime(lon, jdut1)
    print(f'lst {lst*rad:11.7f} gst {gst*rad:11.7f}')

    for i in range(1, 3):
        if i == 1:
            print('\n-------- Neptune test baseline test')
            reci = [1752246215.0, -3759563433.0, -1577568105.0]
            veci = [-18.324, 18.332, 7.777]
            aeci = [0.001, 0.002, 0.003]
            r = reci
            v = veci
            rr = 29.664361 * 149597870.0
            rtasc = 294.98914583 / rad
            decl = -20.8234944 / rad
            drr = (149597870.0 * (29.649616 - 29.664361)) / 86400.0
            drtasc = -0.00000012244 / rad
            ddecl = -0.00000001794 / rad
            reci, veci = radec2rv(rr, rtasc, decl, drr, drtasc, ddecl)
        if i == 2:
            print('\n-------- closer test baseline test')
            rr = 12756.0
            rtasc = 294.98914583 / rad
            decl = -20.8234944 / rad
            drr = 6.798514
            drtasc = -0.00000012244 / rad
            ddecl = -0.00000001794 / rad
            reci, veci = radec2rv(rr, rtasc, decl, drr, drtasc, ddecl)
        print(f'r    {reci[0]:14.7f}{reci[1]:14.7f}{reci[2]:14.7f}', end='')
        print(f' v {veci[0]:14.9f}{veci[1]:14.9f}{veci[2]:14.9f}')

        rr, rtasc, decl, drr, drtasc, ddecl = rv2radec(reci, veci)
        print('            rho km       rtasc deg     decl deg      drho km/s      drtasc deg/s   ddecl deg/s')
        if rtasc < 0.0:
            rtasc = rtasc + twopi
        print(f'radec  {rr:14.7f} {rtasc*rad:14.7f} {decl*rad:14.7f}', end='')
        print(f' {drr:14.7f} {drtasc*rad:14.12f} {ddecl*rad:14.12f}')

        r, v = radec2rv(rr, rtasc, decl, drr, drtasc, ddecl)
        print(f'r    {r[0]:14.7f} {r[1]:14.7f} {r[2]:14.7f}', end='')
        print(f' v {v[0]:14.9f} {v[1]:14.9f} {v[2]:14.9f}')

        # topocentric
        ddpsi = 0.0
        ddeps = 0.0
        trr, trtasc, tdecl, tdrr, tdrtasc, tddecl = rv2tradc(
            reci, veci, latgd, lon, alt, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps)
        print('           trho km      trtasc deg    tdecl deg     tdrho km/s     tdrtasc deg/s  tddecl deg/s')
        if trtasc < 0.0:
            trtasc = trtasc + twopi
        print(f'tradec  {trr:14.7f} {trtasc*rad:14.7f} {tdecl*rad:14.7f}', end='')
        print(f' {tdrr:14.7f} {tdrtasc*rad:14.12f} {tddecl*rad:14.12f}')

        # [r, v] = tradc2rv(...) # Placeholder if implemented
        # print(f'r    {r[0]:14.7f}{r[1]:14.7f}{r[2]:14.7f}', end='')
        # print(f' v {v[0]:14.9f}{v[1]:14.9f}{v[2]:14.9f}')

        # horizon
        rho, az, el, drho, daz, delv = rv2razel(
            reci, veci, latgd, lon, alt, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps)
        if az < 0.0:
            az = az + twopi
        print('rvraz   {0:14.7f} {1:14.7f} {2:14.7f} {3:14.7f} {4:14.12f} {5:14.12f}'.format(
            rho, az*rad, el*rad, drho, daz*rad, delv*rad))
        r, v = razel2rv(
            rho, az, el, drho, daz, delv, latgd, lon, alt, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps)
        print(f'r    {r[0]:14.7f} {r[1]:14.7f} {r[2]:14.7f}', end='')
        print(f' v {v[0]:14.9f} {v[1]:14.9f} {v[2]:14.9f}')

        # ecliptic lat/lon
        rr, elon, elat, drr, delon, delat = rv2ell(reci, veci)
        if elon < 0.0:
            elon = elon + twopi
        print('ell      {0:14.7f} {1:14.7f} {2:14.7f} {3:14.7f} {4:14.12f} {5:14.12f}'.format(
            rr, elon*rad, elat*rad, drr, delon*rad, delat*rad))
        r, v = ell2rv(rr, elon, elat, drr, delon, delat)
        print(f'r    {r[0]:14.7f} {r[1]:14.7f} {r[2]:14.7f}', end='')
        print(f' v {v[0]:14.9f} {v[1]:14.9f} {v[2]:14.9f}')

if __name__ == "__main__":
    ex4_1() 