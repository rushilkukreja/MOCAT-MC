"""
----------------------------------------------------------------------------

    initl.py

    This procedure initializes the spg4 propagator. All the initialization is
    consolidated here instead of having multiple loops inside other routines.

    Author: 
        Jeff Beck (original MATLAB)
        David Vallado (original C++)
        OpenAI Assistant (Python port), 2024

    Inputs:
        ecco       - eccentricity                           0.0 - 1.0
        epoch      - epoch time in days from jan 0, 1950. 0 hr
        inclo      - inclination of satellite
        no         - mean motion of satellite
        satn       - satellite number

    Outputs:
        ainv       - 1.0 / a
        ao         - semi major axis
        con41      - constant
        con42      - 1.0 - 5.0 cos(i)
        cosio      - cosine of inclination
        cosio2     - cosio squared
        einv       - 1.0 / e
        eccsq      - eccentricity squared
        method     - flag for deep space                    'd', 'n'
        omeosq     - 1.0 - ecco * ecco
        posq       - semi-parameter squared
        rp         - radius of perigee
        rteosq     - square root of (1.0 - ecco*ecco)
        sinio      - sine of inclination
        gsto       - gst at time of observation               rad
        no         - mean motion of satellite

    References:
        Hoots, Roehrich, NORAD Spacetrack Report #3 1980
        Hoots, NORAD Spacetrack Report #6 1986
        Hoots, Schumacher and Glover 2004
        Vallado, Crawford, Hujsak, Kelso  2006
----------------------------------------------------------------------------
"""
import numpy as np

def initl(ecco, epoch, inclo, no, satn):
    # WGS-72 earth constants
    # sgp4fix identify constants and allow alternate values
    x2o3 = 2.0 / 3.0
    
    # Calculate auxiliary epoch quantities
    eccsq = ecco * ecco
    omeosq = 1.0 - eccsq
    rteosq = np.sqrt(omeosq)
    cosio = np.cos(inclo)
    cosio2 = cosio * cosio
    
    # Un-kozai the mean motion
    # Note: These constants should be loaded from getgravc or similar
    xke = 60.0 / np.sqrt(6378.135**3 / 398600.8)  # WGS-72 value
    j2 = 0.001082616  # WGS-72 value
    
    ak = (xke / no)**x2o3
    d1 = 0.75 * j2 * (3.0 * cosio2 - 1.0) / (rteosq * omeosq)
    del_val = d1 / (ak * ak)
    adel = ak * (1.0 - del_val * del_val - del_val * (1.0 / 3.0 + 134.0 * del_val * del_val / 81.0))
    del_val = d1 / (adel * adel)
    no = no / (1.0 + del_val)
    
    ao = (xke / no)**x2o3
    sinio = np.sin(inclo)
    po = ao * omeosq
    con42 = 1.0 - 5.0 * cosio2
    con41 = -con42 - cosio2 - cosio2
    ainv = 1.0 / ao
    einv = 1.0 / ecco
    posq = po * po
    rp = ao * (1.0 - ecco)
    method = 'n'
    
    # SGP4fix modern approach to finding sidereal time
    opsmode = 'i'  # Default to improved mode
    if opsmode != 'a':
        gsto = gstime(epoch + 2433281.5)
    else:
        # SGP4fix use old way of finding gst
        # Count integer number of days from 0 jan 1970
        ts70 = epoch - 7305.0
        ids70 = np.floor(ts70 + 1.0e-8)
        tfrac = ts70 - ids70
        # Find greenwich location at epoch
        c1 = 1.72027916940703639e-2
        thgr70 = 1.7321343856509374
        fk5r = 5.07551419432269442e-15
        twopi = 2.0 * np.pi
        c1p2p = c1 + twopi
        gsto = (thgr70 + c1 * ids70 + c1p2p * tfrac + ts70 * ts70 * fk5r) % twopi
    
    if gsto < 0.0:
        gsto = gsto + 2.0 * np.pi
    
    return ainv, ao, con41, con42, cosio, cosio2, einv, eccsq, method, omeosq, posq, rp, rteosq, sinio, gsto, no

# Placeholder for MATLAB dependencies
def gstime(jdut1):
    # TODO: Implement Greenwich sidereal time calculation
    return 0.0 