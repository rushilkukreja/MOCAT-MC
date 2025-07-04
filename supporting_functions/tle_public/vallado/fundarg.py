"""
----------------------------------------------------------------------------

    fundarg.py

    This function calculates the Delaunay variables and planetary values for
    several theories.

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        ttt       - julian centuries of tt
        opt       - method option                  '10', '02', '96', '80'

    Outputs:
        l         - delaunay element               rad
        ll        - delaunay element               rad
        f         - delaunay element               rad
        d         - delaunay element               rad
        omega     - delaunay element               rad
        planetary longitudes                       rad

    References:
        Vallado 2004, 212-214
----------------------------------------------------------------------------
"""
import numpy as np

def fundarg(ttt, opt):
    deg2rad = np.pi / 180.0
    
    # Determine coefficients for iau 2000 nutation theory
    ttt2 = ttt * ttt
    ttt3 = ttt2 * ttt
    ttt4 = ttt2 * ttt2
    
    # IAU 2010 theory
    if opt == '10':
        # Form the delaunay fundamental arguments in deg
        l = 134.96340251 + (1717915923.2178 * ttt + 31.8792 * ttt2 + 
                           0.051635 * ttt3 - 0.00024470 * ttt4) / 3600.0
        ll = 357.52910918 + (129596581.0481 * ttt - 0.5532 * ttt2 - 
                            0.000136 * ttt3 - 0.00001149 * ttt4) / 3600.0
        f = 93.27209062 + (1739527262.8478 * ttt - 12.7512 * ttt2 + 
                          0.001037 * ttt3 + 0.00000417 * ttt4) / 3600.0
        d = 297.85019547 + (1602961601.2090 * ttt - 6.3706 * ttt2 + 
                           0.006593 * ttt3 - 0.00003169 * ttt4) / 3600.0
        omega = 125.04455501 + (-6962890.5431 * ttt + 7.4722 * ttt2 + 
                               0.007702 * ttt3 - 0.00005939 * ttt4) / 3600.0
        
        # Form the planetary arguments in deg
        lonmer = 252.250905494 + 149472.6746358 * ttt
        lonven = 181.979800853 + 58517.8156748 * ttt
        lonear = 100.466448494 + 35999.3728521 * ttt
        lonmar = 355.433274605 + 19140.299314 * ttt
        lonjup = 34.351483900 + 3034.90567464 * ttt
        lonsat = 50.0774713998 + 1222.11379404 * ttt
        lonurn = 314.055005137 + 428.466998313 * ttt
        lonnep = 304.348665499 + 218.486200208 * ttt
        precrate = 1.39697137214 * ttt + 0.0003086 * ttt2
    
    # IAU 2000b theory
    elif opt == '02':
        # Form the delaunay fundamental arguments in deg
        l = 134.96340251 + (1717915923.2178 * ttt) / 3600.0
        ll = 357.52910918 + (129596581.0481 * ttt) / 3600.0
        f = 93.27209062 + (1739527262.8478 * ttt) / 3600.0
        d = 297.85019547 + (1602961601.2090 * ttt) / 3600.0
        omega = 125.04455501 + (-6962890.5431 * ttt) / 3600.0
        
        # Form the planetary arguments in deg
        lonmer = 0.0
        lonven = 0.0
        lonear = 0.0
        lonmar = 0.0
        lonjup = 0.0
        lonsat = 0.0
        lonurn = 0.0
        lonnep = 0.0
        precrate = 0.0
    
    # IAU 1996 theory
    elif opt == '96':
        l = 134.96340251 + (1717915923.2178 * ttt + 31.8792 * ttt2 + 
                           0.051635 * ttt3 - 0.00024470 * ttt4) / 3600.0
        ll = 357.52910918 + (129596581.0481 * ttt - 0.5532 * ttt2 - 
                            0.000136 * ttt3 - 0.00001149 * ttt4) / 3600.0
        f = 93.27209062 + (1739527262.8478 * ttt - 12.7512 * ttt2 + 
                          0.001037 * ttt3 + 0.00000417 * ttt4) / 3600.0
        d = 297.85019547 + (1602961601.2090 * ttt - 6.3706 * ttt2 + 
                           0.006593 * ttt3 - 0.00003169 * ttt4) / 3600.0
        omega = 125.04452222 + (-6962890.2665 * ttt + 7.4722 * ttt2 + 
                               0.007702 * ttt3 - 0.00005939 * ttt4) / 3600.0
        # Form the planetary arguments in deg
        lonmer = 0.0
        lonven = 181.979800853 + 58517.8156748 * ttt
        lonear = 100.466448494 + 35999.3728521 * ttt
        lonmar = 355.433274605 + 19140.299314 * ttt
        lonjup = 34.351483900 + 3034.90567464 * ttt
        lonsat = 50.0774713998 + 1222.11379404 * ttt
        lonurn = 0.0
        lonnep = 0.0
        precrate = 1.39697137214 * ttt + 0.0003086 * ttt2
    
    # IAU 1980 theory
    elif opt == '80':
        l = 134.96298139 + (1717915922.6330 * ttt + 31.310 * ttt2 + 
                           0.064 * ttt3) / 3600.0
        ll = 357.52772333 + (129596581.2240 * ttt - 0.577 * ttt2 - 
                            0.012 * ttt3) / 3600.0
        f = 93.27191028 + (1739527263.1370 * ttt - 13.257 * ttt2 + 
                          0.011 * ttt3) / 3600.0
        d = 297.85036306 + (1602961601.3280 * ttt - 6.891 * ttt2 + 
                           0.019 * ttt3) / 3600.0
        omega = 125.04452222 + (-6962890.5390 * ttt + 7.455 * ttt2 + 
                               0.008 * ttt3) / 3600.0
        # Form the planetary arguments in deg
        lonmer = 252.3 + 149472.0 * ttt
        lonven = 179.9 + 58517.8 * ttt
        lonear = 98.4 + 35999.4 * ttt
        lonmar = 353.3 + 19140.3 * ttt
        lonjup = 32.3 + 3034.9 * ttt
        lonsat = 48.0 + 1222.1 * ttt
        lonurn = 0.0
        lonnep = 0.0
        precrate = 0.0
    
    else:
        raise ValueError(f"Unknown option: {opt}")
    
    # Convert units to rad
    l = (l % 360.0) * deg2rad
    ll = (ll % 360.0) * deg2rad
    f = (f % 360.0) * deg2rad
    d = (d % 360.0) * deg2rad
    omega = (omega % 360.0) * deg2rad
    
    lonmer = (lonmer % 360.0) * deg2rad
    lonven = (lonven % 360.0) * deg2rad
    lonear = (lonear % 360.0) * deg2rad
    lonmar = (lonmar % 360.0) * deg2rad
    lonjup = (lonjup % 360.0) * deg2rad
    lonsat = (lonsat % 360.0) * deg2rad
    lonurn = (lonurn % 360.0) * deg2rad
    lonnep = (lonnep % 360.0) * deg2rad
    precrate = (precrate % 360.0) * deg2rad
    
    return l, ll, f, d, omega, lonmer, lonven, lonear, lonmar, lonjup, lonsat, lonurn, lonnep, precrate 