"""
    -----------------------------------------------------------------
    
                              ex6_10.py
    
  this file demonstrates example 6-10.
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
            25 nov 08  david vallado
                         original
  changes :
            25 nov 08  david vallado
                         original baseline
    
     *****************************************************************
"""

from math import pi
# from noncoplr import noncoplr  # Placeholder for actual function

def ex6_10():
    rad = 180.0 / pi
    re = 6378.137
    print('-------------------- problem ex 6-10')
    aint = 7143.51 / re
    atgt = 42159.4855 / re
    iint = 28.5 / rad
    itgt = 0.0 / rad
    deltai = itgt - iint
    nodeint = 45.0 / rad
    arglatint = 15.0 / rad
    phasenew = pi - arglatint
    truelon = 200.0 / rad
    ktgt = 0
    kint = 1

    # ttrans, tphase, dvphase, dvtrans1, dvtrans2, aphase = noncoplr(phasenew, aint, atgt, ktgt, kint, arglatint, nodeint, truelon, deltai)
    ttrans, tphase, dvphase, dvtrans1, dvtrans2, aphase = 0, 0, 0, 0, 0, 0  # Placeholders
    print('combined maneuver')
    print(f' ttrans  {ttrans:11.7f}')
    print(f' tphase  {tphase:11.7f}')
    print(f' dvphase  {dvphase:11.7f}')
    print(f' dvtrans1  {dvtrans1:11.7f}')
    print(f' dvtrans2  {dvtrans2:11.7f}')
    print(f' aphase  {aphase:11.7f}')

if __name__ == "__main__":
    ex6_10() 