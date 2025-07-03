"""
    -----------------------------------------------------------------
    
                              ex6_1.py
    
  this file demonstrates example 6-1.
    
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
from hohmann import hohmann

def ex6_1():
    rad = 180.0 / pi
    re = 6378.137
    print('-------------------- problem ex 6-1')
    rinit = (re + 191.3411) / re
    rfinal = (re + 35781.34857) / re
    einit = 0.0
    efinal = 0.0
    nuinit = 0.0 / rad
    nufinal = 180.0 / rad

    print('initial position')
    print(f' rinit  {rinit:11.7f}')
    print(f' rfinal {rfinal:11.7f}')
    print(f' einit   {einit:11.7f}')
    print(f' efinal  {efinal:11.7f}')
    print(f' nuinit  {nuinit * rad:11.7f}')
    print(f' nufinal {nufinal * rad:11.7f}')

    deltava, deltavb, dttu = hohmann(rinit, rfinal, einit, efinal, nuinit, nufinal)

    print('hohmann answers')
    print(f' deltava  {deltava:11.7f}')
    print(f' deltavb  {deltavb:11.7f}')
    print(f' dttu  {dttu:11.7f} tu {dttu*13.44685206374:11.7f} sec')

if __name__ == "__main__":
    ex6_1() 