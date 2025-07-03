# ----------------------------------------------------------------------------
#
#                           function adbar2rv
#
#  this function transforms the adbarv elements (rtasc, decl, fpa, azimuth,
#    position and velocity magnitude) into eci position and velocity vectors.
#
#  author        : david vallado                  719-573-2600    9 jun 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    rmag        - eci position vector magnitude  km
#    vmag        - eci velocity vector magnitude  km/sec
#    rtasc       - right ascension of sateillite  rad
#    decl        - declination of satellite       rad
#    fpav        - sat flight path angle from vertrad
#    az          - sat flight path azimuth        rad
#
#  outputs       :
#    r           - eci position vector            km
#    v           - eci velocity vector            km/s
#
#  locals        :
#    none        -
#
#  coupling      :
#    none        -
#
#  references    :
#    vallado       2001, xx
#    chobotov            70
#
# [r,v] = adbar2rv ( rmag,vmag,rtasc,decl,fpav,az );
# ----------------------------------------------------------------------------

import numpy as np

def adbar2rv(rmag, vmag, rtasc, decl, fpav, az):
    """
    Transform the ADBAR elements (rtasc, decl, fpa, azimuth, position and 
    velocity magnitude) into ECI position and velocity vectors.
    
    Args:
        rmag: ECI position vector magnitude (km)
        vmag: ECI velocity vector magnitude (km/sec)
        rtasc: right ascension of satellite (rad)
        decl: declination of satellite (rad)
        fpav: sat flight path angle from vertical (rad)
        az: sat flight path azimuth (rad)
        
    Returns:
        r: ECI position vector (km)
        v: ECI velocity vector (km/s)
    """
    # -------- form position vector
    r = np.zeros(3)
    r[0] = rmag * np.cos(decl) * np.cos(rtasc)
    r[1] = rmag * np.cos(decl) * np.sin(rtasc)
    r[2] = rmag * np.sin(decl)
    
    # -------- form velocity vector
    v = np.zeros(3)
    v[0] = vmag * (np.cos(rtasc) * (-np.cos(az) * np.sin(fpav) * np.sin(decl) + 
                                   np.cos(fpav) * np.cos(decl)) - 
                   np.sin(az) * np.sin(fpav) * np.sin(rtasc))
    v[1] = vmag * (np.sin(rtasc) * (-np.cos(az) * np.sin(fpav) * np.sin(decl) + 
                                   np.cos(fpav) * np.cos(decl)) + 
                   np.sin(az) * np.sin(fpav) * np.cos(rtasc))
    v[2] = vmag * (np.cos(az) * np.cos(decl) * np.sin(fpav) + np.cos(fpav) * np.sin(decl))
    
    return r, v 