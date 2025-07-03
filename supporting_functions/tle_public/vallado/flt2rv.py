# ----------------------------------------------------------------------------
#
#                           function flt2rv
#
#  this function transforms  the flight elements - latgc, lon, fpav, az,
#    position and velocity magnitude into an eci position and velocity vector.
#
#  author        : david vallado                  719-573-2600   17 jun 2002
#
#  revisions
#    vallado     - fix extra terms in rtasc calc                  8 oct 2002
#
#  inputs          description                    range / units
#    rmag        - eci position vector magnitude  km
#    vmag        - eci velocity vector magnitude  km/sec
#    latgc       - geocentric latitude            rad
#    lon         - longitude                      rad
#    fpa         - sat flight path angle          rad
#    az          - sat flight path az             rad
#    ttt         - julian centuries of tt         centuries
#    jdut1       - julian date of ut1             days from 4713 bc
#    lod         - excess length of day           sec
#    xp          - polar motion coefficient       arc sec
#    yp          - polar motion coefficient       arc sec
#    terms       - number of terms for ast calculation 0,2
#    ddpsi,ddeps - corrections for fk5 to gcrf    rad
#
#  outputs       :
#    r           - eci position vector            km
#    v           - eci velocity vector            km/s
#
#  locals        :
#    fpav        - sat flight path anglefrom vert rad
#
#  coupling      :
#    none        -
#
#  references    :
#    vallado       2001, xx
#    chobotov            67
#
# [r,v] = flt2rv ( rmag,vmag,latgc,lon,fpa,az,ttt,jdut1,lod,xp,yp,terms,ddpsi,ddeps );
# ----------------------------------------------------------------------------

import numpy as np

def flt2rv(rmag, vmag, latgc, lon, fpa, az, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps):
    """
    Transform the flight elements - latgc, lon, fpav, az, position and 
    velocity magnitude into an ECI position and velocity vector.
    
    Args:
        rmag: ECI position vector magnitude (km)
        vmag: ECI velocity vector magnitude (km/sec)
        latgc: geocentric latitude (rad)
        lon: longitude (rad)
        fpa: sat flight path angle (rad)
        az: sat flight path azimuth (rad)
        ttt: julian centuries of tt (centuries)
        jdut1: julian date of ut1 (days from 4713 bc)
        lod: excess length of day (sec)
        xp: polar motion coefficient (arc sec)
        yp: polar motion coefficient (arc sec)
        terms: number of terms for ast calculation 0,2
        ddpsi: corrections for fk5 to gcrf (rad)
        ddeps: corrections for fk5 to gcrf (rad)
        
    Returns:
        r: ECI position vector (km)
        v: ECI velocity vector (km/s)
    """
    twopi = 2.0 * np.pi
    small = 0.00000001
    
    # -------- form position vector
    recef = np.zeros(3)
    recef[0] = rmag * np.cos(latgc) * np.cos(lon)
    recef[1] = rmag * np.cos(latgc) * np.sin(lon)
    recef[2] = rmag * np.sin(latgc)
    
    # -------- convert r to eci
    vecef = np.zeros(3)
    aecef = np.zeros(3)
    
    # TODO: Implement ecef2eci function
    # [r, v, a] = ecef2eci(recef, vecef, aecef, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps)
    r = recef  # Placeholder
    v = np.zeros(3)  # Placeholder
    a = np.zeros(3)  # Placeholder
    
    # ------------- calculate rtasc and decl ------------------
    temp = np.sqrt(r[0] * r[0] + r[1] * r[1])
    
    # v needs to be defined here
    if temp < small:
        rtasc = np.arctan2(v[1], v[0])
    else:
        rtasc = np.arctan2(r[1], r[0])
    
    decl = np.arcsin(r[2] / rmag)
    
    # -------- form velocity vector
    fpav = np.pi * 0.5 - fpa
    v[0] = vmag * (np.cos(rtasc) * (-np.cos(az) * np.sin(fpav) * np.sin(decl) + 
                                   np.cos(fpav) * np.cos(decl)) - 
                   np.sin(az) * np.sin(fpav) * np.sin(rtasc))
    v[1] = vmag * (np.sin(rtasc) * (-np.cos(az) * np.sin(fpav) * np.sin(decl) + 
                                   np.cos(fpav) * np.cos(decl)) + 
                   np.sin(az) * np.sin(fpav) * np.cos(rtasc))
    v[2] = vmag * (np.cos(az) * np.cos(decl) * np.sin(fpav) + np.cos(fpav) * np.sin(decl))
    
    return r, v 