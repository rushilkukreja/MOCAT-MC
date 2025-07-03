"""
    -----------------------------------------------------------------
    
                              ex11_1.py
    
  this file demonstrates example 11-1.
    
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
# from satfov import satfov  # Placeholder for actual function

def ex11_1():
    # --------  satfov calculations
    incl = 40.0 / rad
    az = 40.0 / rad
    slatgd = 50.0 / rad
    slon = 40.0 / rad
    salt = 800.0  # km
    tfov = 25.0 / rad
    etactr = 0.0 / rad
    fovmax = 60.0 / rad

    # totalrng, rhomax, rhomin, tgtlat, tgtlon = satfov(incl, az, slatgd, slon, salt, tfov, etactr, fovmax)
    totalrng, rhomax, rhomin, tgtlat, tgtlon = [0]*5  # Placeholder
    print('satfov results:')
    print(f'totalrng={totalrng}, rhomax={rhomax}, rhomin={rhomin}, tgtlat={tgtlat}, tgtlon={tgtlon}')

if __name__ == "__main__":
    ex11_1() 