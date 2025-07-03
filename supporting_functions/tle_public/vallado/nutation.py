# ----------------------------------------------------------------------------
#
#                           function nutation
#
#  this function calulates the transformation matrix that accounts for the
#    effects of nutation.
#
#  author        : david vallado                  719-573-2600   27 jun 2002
#
#  revisions
#    vallado     - consolidate with iau 2000                     14 feb 2005
#
#  inputs          description                    range / units
#    ttt         - julian centuries of tt
#    ddpsi       - delta psi correction to gcrf   rad
#    ddeps       - delta eps correction to gcrf   rad
#
#  outputs       :
#    deltapsi    - nutation angle                 rad
#    trueeps     - true obliquity of the ecliptic rad
#    meaneps     - mean obliquity of the ecliptic rad
#    omega       -                                rad
#    nut         - transformation matrix for tod - mod
#
#  locals        :
#    iar80       - integers for fk5 1980
#    rar80       - reals for fk5 1980
#    ttt2        - ttt squared
#    ttt3        - ttt cubed
#    l           -                                rad
#    ll          -                                rad
#    f           -                                rad
#    d           -                                rad
#    deltaeps    - change in obliquity            rad
#
#  coupling      :
#    fundarg     - find fundamental arguments
#
#  references    :
#    vallado       2004, 221-222
#
# [deltapsi, trueeps, meaneps, omega,nut] = nutation  (ttt,ddpsi,ddeps );
# ----------------------------------------------------------------------------

import numpy as np

def nutation(ttt, ddpsi, ddeps):
    """
    Calculate the transformation matrix that accounts for the effects of nutation.
    
    Args:
        ttt: julian centuries of tt
        ddpsi: delta psi correction to gcrf (rad)
        ddeps: delta eps correction to gcrf (rad)
        
    Returns:
        deltapsi: nutation angle (rad)
        trueeps: true obliquity of the ecliptic (rad)
        meaneps: mean obliquity of the ecliptic (rad)
        omega: omega value (rad)
        nut: transformation matrix for tod - mod
    """
    deg2rad = np.pi / 180.0
    
    # TODO: Implement iau80in function
    # [iar80, rar80] = iau80in()  # coeff in deg
    
    # Placeholder for iau80in coefficients
    iar80 = np.zeros((106, 5))  # Placeholder
    rar80 = np.zeros((106, 4))  # Placeholder
    
    # ---- determine coefficients for iau 1980 nutation theory ----
    ttt2 = ttt * ttt
    ttt3 = ttt2 * ttt
    
    meaneps = -46.8150 * ttt - 0.00059 * ttt2 + 0.001813 * ttt3 + 84381.448
    meaneps = np.remainder(meaneps / 3600.0, 360.0)
    meaneps = meaneps * deg2rad
    
    # TODO: Implement fundarg function
    # [l, l1, f, d, omega, lonmer, lonven, lonear, lonmar, lonjup, lonsat, lonurn, lonnep, precrate] = fundarg(ttt, '80')
    
    # Placeholder for fundarg results
    l = 0.0
    l1 = 0.0
    f = 0.0
    d = 0.0
    omega = 0.0
    
    deltapsi = 0.0
    deltaeps = 0.0
    for i in range(105, -1, -1):  # 106:-1:1 in MATLAB
        tempval = (iar80[i, 0] * l + iar80[i, 1] * l1 + iar80[i, 2] * f + 
                   iar80[i, 3] * d + iar80[i, 4] * omega)
        deltapsi = deltapsi + (rar80[i, 0] + rar80[i, 1] * ttt) * np.sin(tempval)
        deltaeps = deltaeps + (rar80[i, 2] + rar80[i, 3] * ttt) * np.cos(tempval)
    
    # --------------- find nutation parameters --------------------
    deltapsi = np.remainder(deltapsi + ddpsi / deg2rad, 360.0) * deg2rad
    deltaeps = np.remainder(deltaeps + ddeps / deg2rad, 360.0) * deg2rad
    trueeps = meaneps + deltaeps
    
    cospsi = np.cos(deltapsi)
    sinpsi = np.sin(deltapsi)
    coseps = np.cos(meaneps)
    sineps = np.sin(meaneps)
    costrueeps = np.cos(trueeps)
    sintrueeps = np.sin(trueeps)
    
    nut = np.zeros((3, 3))
    nut[0, 0] = cospsi
    nut[0, 1] = costrueeps * sinpsi
    nut[0, 2] = sintrueeps * sinpsi
    nut[1, 0] = -coseps * sinpsi
    nut[1, 1] = costrueeps * coseps * cospsi + sintrueeps * sineps
    nut[1, 2] = sintrueeps * coseps * cospsi - sineps * costrueeps
    nut[2, 0] = -sineps * sinpsi
    nut[2, 1] = costrueeps * sineps * cospsi - sintrueeps * coseps
    nut[2, 2] = sintrueeps * sineps * cospsi + costrueeps * coseps
    
    return deltapsi, trueeps, meaneps, omega, nut 