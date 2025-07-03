# ------------------------------------------------------------------------------
#
#                           function pathm
#
#  this function determines the end position for a given range and azimuth
#    from a given point.
#
#  author        : david vallado                  719-573-2600   27 may 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    llat        - start geocentric latitude      -pi/2 to  pi/2 rad
#    llon        - start longitude (west -)       0.0  to 2pi rad
#    range       - range between points           er
#    az          - azimuth                        0.0  to 2pi rad
#
#  outputs       :
#    tlat        - end geocentric latitude        -pi/2 to  pi/2 rad
#    tlon        - end longitude (west -)         0.0  to 2pi rad
#
#  locals        :
#    sindeltan   - sine of delta n                rad
#    cosdeltan   - cosine of delta n              rad
#    deltan      - angle between the two points   rad
#
#  coupling      :
#    none.
#
#  references    :
#    vallado       2001, 774-776, eq 11-6, eq 11-7
#
# [tlat,tlon] = pathm ( llat, llon, range, az );
# ------------------------------------------------------------------------------

import numpy as np

def pathm(llat, llon, range_val, az):
    """
    Determine the end position for a given range and azimuth from a given point.
    
    Args:
        llat: start geocentric latitude (-pi/2 to pi/2 rad)
        llon: start longitude (west -) (0.0 to 2pi rad)
        range_val: range between points (er)
        az: azimuth (0.0 to 2pi rad)
        
    Returns:
        tlat: end geocentric latitude (-pi/2 to pi/2 rad)
        tlon: end longitude (west -) (0.0 to 2pi rad)
    """
    twopi = 2.0 * np.pi
    
    # -------------------------  implementation   -----------------
    small = 0.00000001
    
    az = np.remainder(az, twopi)
    if llon < 0.0:
        llon = twopi + llon
    
    if range_val > twopi:
        range_val = np.remainder(range_val, twopi)
    
    # ----------------- find geocentric latitude  -----------------
    tlat = np.arcsin(np.sin(llat) * np.cos(range_val) + np.cos(llat) * np.sin(range_val) * np.cos(az))
    
    # ---- find delta n, the angle between the points -------------
    if (abs(np.cos(tlat)) > small) and (abs(np.cos(llat)) > small):
        sindn = np.sin(az) * np.sin(range_val) / np.cos(tlat)
        cosdn = (np.cos(range_val) - np.sin(tlat) * np.sin(llat)) / (np.cos(tlat) * np.cos(llat))
        deltan = np.arctan2(sindn, cosdn)
    else:
        # ------ case where launch is within 3nm of a pole --------
        if abs(np.cos(llat)) <= small:
            if (range_val > np.pi) and (range_val < twopi):
                deltan = az + np.pi
            else:
                deltan = az
        
        # ----- case where end point is within 3nm of a pole ------
        if abs(np.cos(tlat)) <= small:
            deltan = 0.0
    
    tlon = llon + deltan
    if abs(tlon) > twopi:
        tlon = np.remainder(tlon, twopi)
    
    if tlon < 0.0:
        tlon = twopi + tlon
    
    return tlat, tlon 