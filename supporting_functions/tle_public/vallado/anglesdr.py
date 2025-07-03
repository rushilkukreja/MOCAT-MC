import numpy as np

def anglesdr(decl1, decl2, decl3, rtasc1, rtasc2, rtasc3, jd1, jd2, jd3, rsite1, rsite2, rsite3):
    """
    This function solves the problem of orbit determination using three
    optical sightings. The solution function uses the double-r technique.
    
    Author: David Vallado 719-573-2600 1 mar 2001
    8 oct 2007
    
    Inputs:
        rtasc1 - right ascension #1 (rad)
        rtasc2 - right ascension #2 (rad)
        rtasc3 - right ascension #3 (rad)
        decl1 - declination #1 (rad)
        decl2 - declination #2 (rad)
        decl3 - declination #3 (rad)
        jd1 - julian date of 1st sighting (days from 4713 bc)
        jd2 - julian date of 2nd sighting (days from 4713 bc)
        jd3 - julian date of 3rd sighting (days from 4713 bc)
        rsite1, rsite2, rsite3 - ijk site position vectors (km)
    
    Outputs:
        r2 - ijk position vector at t2 (km)
        v2 - ijk velocity vector at t2 (km/s)
    
    References:
        Vallado 2007, 439-443
    """
    def mag(vec):
        return np.linalg.norm(vec)
    
    def dot(vec1, vec2):
        return np.dot(vec1, vec2)
    
    def cross(vec1, vec2):
        return np.cross(vec1, vec2)
    
    def rv2coe(r, v):
        # Placeholder for rv2coe function
        return None, None, None, None, None, None, None, None, None, None, None
    
    def doubler(cc1, cc2, magrsite1, magrsite2, magr1in, magr2in, los1, los2, los3, rsite1, rsite2, rsite3, t1, t3, direct):
        # Placeholder for doubler function
        return None, None, None, None, None, None, None, None
    
    # Constants
    re = 6378.137
    mu = 3.986004418e5
    rad = 57.29577951308230
    
    magr1in = 2.0 * re
    magr2in = 2.01 * re
    direct = 'y'
    
    tol = 1e-8 * re  # km
    pctchg = 0.005
    
    # Subtract dates and convert fraction of day to seconds
    t1 = (jd1 - jd2) * 86400.0  # secs
    t3 = (jd3 - jd2) * 86400.0
    
    # Form line of sight vectors
    los1 = np.array([np.cos(decl1) * np.cos(rtasc1), np.cos(decl1) * np.sin(rtasc1), np.sin(decl1)])
    los2 = np.array([np.cos(decl2) * np.cos(rtasc2), np.cos(decl2) * np.sin(rtasc2), np.sin(decl2)])
    los3 = np.array([np.cos(decl3) * np.cos(rtasc3), np.cos(decl3) * np.sin(rtasc3), np.sin(decl3)])
    
    # Now we're ready to start the actual double r algorithm
    magr1old = 99999.9
    magr2old = 99999.9
    magrsite1 = mag(rsite1)
    magrsite2 = mag(rsite2)
    magrsite3 = mag(rsite3)
    
    # Take away negatives because escobal defines rs opposite
    cc1 = 2.0 * dot(los1, rsite1)
    cc2 = 2.0 * dot(los2, rsite2)
    ktr = 0
    
    # Main loop to get three values of the double-r for processing
    while abs(magr1in - magr1old) > tol or abs(magr2in - magr2old) > tol:
        ktr = ktr + 1
        print(f'{ktr:2d} ', end='')
        
        r2, r3, f1, f2, q1, magr1, magr2, a, deltae32 = doubler(cc1, cc2, magrsite1, magrsite2, magr1in, magr2in,
                                                               los1, los2, los3, rsite1, rsite2, rsite3, t1, t3, direct)
        
        # Check intermediate status
        f = 1.0 - a / magr2 * (1.0 - np.cos(deltae32))
        g = t3 - np.sqrt(a**3 / mu) * (deltae32 - np.sin(deltae32))
        v2 = (r3 - f * r2) / g
        p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = rv2coe(r2, v2)
        print(f'coes {p:11.4f}{a:11.4f}{ecc:13.9f}{incl*rad:13.7f}{omega*rad:11.5f}{argp*rad:11.5f}{nu*rad:11.5f}{m*rad:11.5f}')
        
        # Re-calculate f1 and f2 with r1 = r1 + delta r1
        magr1o = magr1in
        magr1in = (1.0 + pctchg) * magr1in
        deltar1 = pctchg * magr1in
        r2, r3, f1delr1, f2delr1, q2, magr1, magr2, a, deltae32 = doubler(cc1, cc2, magrsite1, magrsite2, magr1in, magr2in,
                                                                          los1, los2, los3, rsite1, rsite2, rsite3, t1, t3, direct)
        pf1pr1 = (f1delr1 - f1) / deltar1
        pf2pr1 = (f2delr1 - f2) / deltar1
        
        # Re-calculate f1 and f2 with r2 = r2 + delta r2
        magr1in = magr1o
        deltar1 = pctchg * magr1in
        magr2o = magr2in
        magr2in = (1.0 + pctchg) * magr2in
        deltar2 = pctchg * magr2in
        r2, r3, f1delr2, f2delr2, q3, magr1, magr2, a, deltae32 = doubler(cc1, cc2, magrsite1, magrsite2, magr1in, magr2in,
                                                                          los1, los2, los3, rsite1, rsite2, rsite3, t1, t3, direct)
        pf1pr2 = (f1delr2 - f1) / deltar2
        pf2pr2 = (f2delr2 - f2) / deltar2
        
        # Now calculate an update
        magr2in = magr2o
        deltar2 = pctchg * magr2in
        
        delta = pf1pr1 * pf2pr2 - pf2pr1 * pf1pr2
        delta1 = pf2pr2 * f1 - pf1pr2 * f2
        delta2 = pf1pr1 * f2 - pf2pr1 * f1
        
        deltar1 = -delta1 / delta
        deltar2 = -delta2 / delta
        
        magr1old = magr1in
        magr2old = magr2in
        
        # May need to limit the amount of the correction
        if abs(deltar1) > magr1in * pctchg:
            print(f'{deltar1:11.7f}')
        
        if abs(deltar2) > magr2in * pctchg:
            print(f'{deltar2:11.7f}')
        
        magr1in = magr1in + deltar1
        magr2in = magr2in + deltar2
        
        print(f'qs {q1:11.7f}  {q2:11.7f}  {q3:11.7f}')
        print(f'magr1o {magr1o:11.7f} delr1 {deltar1:11.7f} magr1 {magr1in:11.7f} {magr1old:11.7f}')
        print(f'magr2o {magr2o:11.7f} delr2 {deltar2:11.7f} magr2 {magr2in:11.7f} {magr2old:11.7f}')
        print('===============================================')
    
    # Needed to get the r2 set properly since the last one was moving r2
    r2, r3, f1, f2, q1, magr1, magr2, a, deltae32 = doubler(cc1, cc2, magrsite1, magrsite2, magr1in, magr2in,
                                                          los1, los2, los3, rsite1, rsite2, rsite3, t1, t3, direct)
    
    f = 1.0 - a / magr2 * (1.0 - np.cos(deltae32))
    g = t3 - np.sqrt(a**3 / mu) * (deltae32 - np.sin(deltae32))
    v2 = (r3 - f * r2) / g
    
    return r2, v2 