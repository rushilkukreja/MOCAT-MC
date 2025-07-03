"""
    -----------------------------------------------------------------
    
                              ex11_4.py
    
  this file demonstrates example 11-4.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
            30 aug 11  david vallado
                         original
  changes :
            22 aug 11 david vallado
                         original baseline
    
     *****************************************************************
"""

from constmath import *
from constastro import *
import numpy as np

def ex11_4():
    # --------  repeat gt calculations
    j2 = 0.00108263
    a = 6570.3358  # km
    ecc = 0.006301
    incl = 45.00 / rad
    p = a * (1.0 - ecc * ecc)
    nanom = np.sqrt(mu / (a * a * a))
    print(f'p {p:11.7f}  {p/re:11.7f}')
    n = nanom
    print(f'n {n:11.7f}  {n/rad:11.7f}')
    raanrate = -1.5 * j2 * re**2 * n * np.cos(incl) / (p * p)
    print(f'raanrate {raanrate:11.7f}  {raanrate*180*86400/np.pi:11.7f}')
    deltatoa = (3.0 * np.pi / (n * a)) * (1.0 + 0.5 * j2 * (re / a)**2 * (4.0 * np.cos(incl)**2 - 1.0))
    print(f'deltatoa {deltatoa:11.7f}  {deltatoa*re/tusec:11.7f}')
    deltaOdotoa = -3.5 * raanrate / a
    print(f'deltaOdotoa {deltaOdotoa:11.7f}  {deltaOdotoa*re/tusec:11.7f}')
    deltapoi = 12.0 * np.pi / n * j2 * (re / a)**2 * np.sin(2.0 * incl)
    print(f'deltapoi {deltapoi:11.7f}  {deltapoi/tusec:11.7f}')
    deltaraanoi = -raanrate * np.tan(incl)
    print(f'deltaraanoi {deltaraanoi:11.7f}  {deltaraanoi/tusec:11.7f}')
    pnodal = 2.0 * np.pi / n
    print(f'pnodal {pnodal:11.7f} s {pnodal/60.0:11.7f} min')
    anomper = pnodal * (1.0 / (1.0 + 0.75 * j2 * (re / p)**2 * (np.sqrt(1.0 - ecc * ecc) * (2.0 - 3.0 * np.sin(incl)**2) + (4.0 - 5.0 * np.sin(incl)**2))))
    print(f'anomper {anomper:11.7f} s {anomper/60.0:11.7f} min')
    dellon = (omegaearth - raanrate) * anomper
    print(f'dellon {dellon:11.7f}  {dellon*re:11.7f}')
    dlpa = re * (omegaearth - raanrate) * deltatoa - deltaOdotoa * re * anomper
    print(f'dlpa {dlpa:11.7f}  {dlpa:11.7f}')
    dlpi = re * (omegaearth - raanrate) * deltapoi - deltaraanoi * re * anomper
    print(f'dlpi {dlpi:11.7f}  {dlpi:11.7f}')
    dadt = -0.174562 / anomper
    didt = 0.000132 * np.pi / (180 * anomper)
    print(f'dadt {dadt*anomper:11.7f}  {dadt:11.7f}')
    print(f'didt {didt*anomper*180/np.pi:11.7f}  {didt:11.7f}')
    k2 = 1.0 / anomper * (dlpa * dadt + dlpi * didt)
    k1 = np.sqrt(2.0 * k2 * (-50 - 50))
    print(f'k2 {k2:11.7f}  {k2*tusec/re:11.7f}')
    print(f'k1 {k1:11.7f}  {k1*tusec/re:11.7f}')
    da = k1 * anomper / dlpa
    print(f'da {da:11.7f}  {da:11.7f}')
    tdrift = -k1 / k2
    print(f'tdrift {tdrift:11.7f}  {tdrift/60.0:11.7f}')
    deltav = n * 0.5 * da
    print(f'deltav {deltav:11.7f}  {deltav:11.7f}')
    # x = x/0  # MATLAB code triggers error here, can be omitted in Python

if __name__ == "__main__":
    ex11_4() 