"""
    -----------------------------------------------------------------
    
                              Ex5_1.py
    
  this file demonstrates example 5-1.
    
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

from constmath import *
from jday import jday
from sun import sun
from mag import mag
from mod2eci import mod2eci
from hms2rad import hms2rad
from dms2rad import dms2rad

def ex5_1():
    jd = jday(2006, 4, 2, 0, 0, 0.0)
    print(f'jd  {jd:11.9f}')

    rsun, rtasc, decl = sun(jd)
    print(f'sun  rtasc {rtasc*rad:14.6f} deg decl {decl*rad:14.6f} deg')
    print(f'sun MOD {rsun[0]:11.9f}{rsun[1]:11.9f}{rsun[2]:11.9f} au')
    print(f'sun MOD {rsun[0]*149597870.0:14.4f}{rsun[1]*149597870.0:14.4f}{rsun[2]*149597870.0:14.4f} km')

    rsunaa = [0.9776872, 0.1911521, 0.0828717]
    rsunaa_km = [x * 149597870.0 for x in rsunaa]
    print(f'rs aa ICRF {rsunaa_km[0]:11.9f} {rsunaa_km[1]:11.9f} {rsunaa_km[2]:11.9f} km')

    da = [rsun[i]*149597870.0 - rsunaa_km[i] for i in range(3)]
    print(f'delta mod,eci  {da[0]:11.9f} {da[1]:11.9f} {da[2]:11.9f} {mag(da):11.4f} km')

    ttt = (jd - 2451545.0) / 36525.0
    vmod = [0, 0, 0]
    amod = [0, 0, 0]
    reci, veci, aeci = mod2eci(rsun, vmod, amod, ttt)

    db = [reci[i]*149597870.0 - rsunaa_km[i] for i in range(3)]
    print(f'delta ~eci,eci  {db[0]:11.9f} {db[1]:11.9f} {db[2]:11.9f} {mag(db):11.4f} km {mag(db)/149597870.0:11.4f} au')

    hms = hms2rad(0, 44, 33.42)
    dms = dms2rad(4, 47, 18.3)
    print(f'hms ast alm rtasc {hms*rad:11.9f} decl {dms*rad:11.9f}')

if __name__ == "__main__":
    ex5_1() 