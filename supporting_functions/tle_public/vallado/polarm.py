# ----------------------------------------------------------------------------
#
#                           function polarm
#
#  this function calulates the transformation matrix that accounts for polar
#    motion. both the 1980 and 2000 theories are handled. note that the rotation 
#    order is different between 1980 and 2000 .
#
#  author        : david vallado                  719-573-2600   25 jun 2002
#
#  revisions
#    vallado     - consolidate with iau 2000                     14 feb 2005
#
#  inputs          description                    range / units
#    xp          - polar motion coefficient       arcsec
#    yp          - polar motion coefficient       arcsec
#    ttt         - julian centuries of tt (00 theory only)
#    opt         - method option                  '01', '02', '80'
#
#  outputs       :
#    pm          - transformation matrix for ecef - pef
#
#  locals        :
#    convrt      - conversion from arcsec to rad
#    sp          - s prime value
#
#  coupling      :
#    none.
#
#  references    :
#    vallado       2004, 207-209, 211, 223-224
#
# [pm] = polarm ( xp, yp, ttt, opt );
# ----------------------------------------------------------------------------

import numpy as np

def polarm(xp, yp, ttt, opt):
    """
    Calculate the transformation matrix that accounts for polar motion.
    Both the 1980 and 2000 theories are handled. Note that the rotation 
    order is different between 1980 and 2000.
    
    Args:
        xp: polar motion coefficient (arcsec)
        yp: polar motion coefficient (arcsec)
        ttt: julian centuries of tt (00 theory only)
        opt: method option ('01', '02', '80')
        
    Returns:
        pm: transformation matrix for ecef - pef
    """
    convrt = np.pi / (3600.0 * 180.0)
    
    xp = xp * convrt
    yp = yp * convrt
    
    cosxp = np.cos(xp)
    sinxp = np.sin(xp)
    cosyp = np.cos(yp)
    sinyp = np.sin(yp)
    
    pm = np.zeros((3, 3))
    
    if opt == '80':
        pm[0, 0] = cosxp
        pm[0, 1] = 0.0
        pm[0, 2] = -sinxp
        pm[1, 0] = sinxp * sinyp
        pm[1, 1] = cosyp
        pm[1, 2] = cosxp * sinyp
        pm[2, 0] = sinxp * cosyp
        pm[2, 1] = -sinyp
        pm[2, 2] = cosxp * cosyp
        
        # a1 = rot2mat(xp)
        # a2 = rot1mat(yp)
        # pm = a2*a1
        # Approximate matrix using small angle approximations
        # pm[0, 0] = 1.0
        # pm[1, 0] = 0.0
        # pm[2, 0] = xp
        # pm[0, 1] = 0.0
        # pm[1, 1] = 1.0
        # pm[2, 1] = -yp
        # pm[0, 2] = -xp
        # pm[1, 2] = yp
        # pm[2, 2] = 1.0
    else:
        # approximate sp value in rad
        sp = -47.0e-6 * ttt * convrt
        cossp = np.cos(sp)
        sinsp = np.sin(sp)
        
        # form the matrix
        pm[0, 0] = cosxp * cossp
        pm[0, 1] = -cosyp * sinsp + sinyp * sinxp * cossp
        pm[0, 2] = -sinyp * sinsp - cosyp * sinxp * cossp
        pm[1, 0] = cosxp * sinsp
        pm[1, 1] = cosyp * cossp + sinyp * sinxp * sinsp
        pm[1, 2] = sinyp * cossp - cosyp * sinxp * sinsp
        pm[2, 0] = sinxp
        pm[2, 1] = -sinyp * cosxp
        pm[2, 2] = cosyp * cosxp
        
        # a1 = rot1mat(yp)
        # a2 = rot2mat(xp)
        # a3 = rot3mat(-sp)
        # pm = a3*a2*a1
    
    return pm 