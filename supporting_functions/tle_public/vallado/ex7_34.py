"""
    -----------------------------------------------------------------
    
                              ex7_34.py
    
  this file demonstrates example 7-3 and 7-4. it also compares the gibbs and 
  herrick gibbs approaches. 
    
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
from constastro import *
# Placeholder imports for functions to be implemented
# from gibbs import gibbs
# from hgibbs import hgibbs
# from mag import mag
# from coe2rv import coe2rv
# from kepler import kepler

def ex7_34():
    print('-------------------- problem ex 7-3')
    r1 = np.array([0.0, 0.0, 6378.137])
    r2 = np.array([0.0, -4464.696, -5102.509])
    r3 = np.array([0.0, 5740.323, 3189.068])
    print(f' r1 {r1[0]:15.10f}  {r1[1]:15.10f}  {r1[2]:15.10f}')
    print(f' r2 {r2[0]:15.10f}  {r2[1]:15.10f}  {r2[2]:15.10f}')
    print(f' r3 {r3[0]:15.10f}  {r3[1]:15.10f}  {r3[2]:15.10f}')

    # v2g, theta, theta1, copa, errorg = gibbs(r1, r2, r3)
    v2g, theta, theta1, copa, errorg = np.zeros(3), 0, 0, 0, 0  # Placeholder
    print(f' v2g {v2g[0]:15.9f}   {v2g[1]:15.9f}   {v2g[2]:15.9f} km/s \n\n\n')

    print('-------------------- problem ex 7-4')
    r1 = np.array([3419.85564, 6019.82602, 2784.60022])
    r2 = np.array([2935.91195, 6326.18324, 2660.59584])
    r3 = np.array([2434.95202, 6597.38674, 2521.52311])
    print(f' r1 {r1[0]:15.10f}  {r1[1]:15.10f}  {r1[2]:15.10f}')
    print(f' r2 {r2[0]:15.10f}  {r2[1]:15.10f}  {r2[2]:15.10f}')
    print(f' r3 {r3[0]:15.10f}  {r3[1]:15.10f}  {r3[2]:15.10f}')

    jd1 = 0.0 / 86400.0
    jd2 = (60.0 + 16.48) / 86400.0
    jd3 = (120.0 + 33.04) / 86400.0

    # v2h, theta, theta1, copa, errorh = hgibbs(r1, r2, r3, jd1, jd2, jd3)
    v2h, theta, theta1, copa, errorh = np.zeros(3), 0, 0, 0, 0  # Placeholder
    print(f' v2h {v2h[0]:15.9f}   {v2h[1]:15.9f}   {v2h[2]:15.9f} km/s \n\n\n')

    # The rest of the code compares gibbs and hgibbs
    print('-------------------- compare gibbs and hgibbs')
    # constmath, constastro already imported
    r = np.array([1.0, 0.10, 0.9760]) * re
    magr = 0  # mag(r) # Placeholder
    v = np.array([0.3, 0.10, 0.2760]) * velkmps
    magv = 0  # mag(v) # Placeholder
    p = 6.61 * re
    ecc = 0.0
    incl = 34.0 / rad
    omega = 0.0
    argp = 0.0
    nu = 0.0
    arglat = 0.0
    truelon = 0.0
    lonper = 0.0
    # r, v = coe2rv(p, ecc, incl, omega, argp, nu, arglat, truelon, lonper)
    r, v = np.zeros(3), np.zeros(3)  # Placeholder

    # Use kepler propagation
    # for i in range(0, 51):
    #     r1, v1, error = kepler(r, v, i * 600.0)
    #     print(f'{i:4d} x {r1[0]:11.7f}  {r1[1]:11.7f}  {r1[2]:11.7f}  {v1[0]:11.7f}  {v1[1]:11.7f}  {v1[2]:11.7f}')

    # Test gibbs hgibbs accuracies against two body orbits
    i = 1
    t2 = 0.0  # min
    # magr = mag(r)
    # magv = mag(v)
    rdotv = 0  # np.dot(r, v) # Placeholder

    # -------------  find sme, alpha, and a  ------------------
    sme = 0  # ((magv ** 2) * 0.5) - (mu / magr) # Placeholder
    a = 0    # -mu / (2.0 * sme) # Placeholder
    period = 0  # twopi * np.sqrt(abs(a) ** 3.0 / mu) # sec, Placeholder

    print(' ktr    dt sec   fraction       ang1          ang2       coplanar        gibbs      err flg             hgibbs      errflg ')
    while t2 < (period * 0.45 if period else 1):  # Placeholder for period
        if t2 < (period * 0.001 if period else 0.001):
            t2 = t2 + (period * 0.00005 if period else 0.00005)
        elif t2 < (period * 0.006 if period else 0.006):
            t2 = t2 + (period * 0.001 if period else 0.001)
        elif t2 < (period * 0.015 if period else 0.015):
            t2 = t2 + (period * 0.005 if period else 0.005)
        elif t2 < (period * 0.20 if period else 0.20):
            t2 = t2 + (period * 0.01 if period else 0.01)
        else:
            t2 = t2 + (period * 0.05 if period else 0.05)

        t1 = 0.0
        t3 = 2.0 * t2

        # r1, v1, error = kepler(r, v, t1)
        # r2, v2, error = kepler(r, v, t2)
        # r3, v3, error = kepler(r, v, t3)
        r1, v1, r2, v2, r3, v3 = [np.zeros(3) for _ in range(6)]  # Placeholders

        # v2g, theta, theta1, copa, errorg = gibbs(r1, r2, r3)
        v2g, theta, theta1, copa, errorg = np.zeros(3), 0, 0, 0, 0  # Placeholder
        jd1 = t1 / 86400.0
        jd2 = t2 / 86400.0
        jd3 = t3 / 86400.0
        # v2h, theta, theta1, copa, errorh = hgibbs(r1, r2, r3, jd1, jd2, jd3)
        v2h, theta, theta1, copa, errorh = np.zeros(3), 0, 0, 0, 0  # Placeholder

        # tempg = v2g - v2
        # temph = v2h - v2
        magtempg = 0  # np.linalg.norm(tempg)
        magtemph = 0  # np.linalg.norm(temph)
        print(f'{i:3d} {t2:11.3f} {t2/(period if period else 1):8.4f}  {theta*rad:12.6f} {theta1*rad:12.6f} {copa*rad:10.5f} dg {magtempg*1000:14.9f} {str(errorg):12s} dh {magtemph*1000:14.9f} m/s {str(errorh):12s}')
        i += 1
        if period == 0 and t2 > 0.2:
            break  # Prevent infinite loop in placeholder mode

if __name__ == "__main__":
    ex7_34() 