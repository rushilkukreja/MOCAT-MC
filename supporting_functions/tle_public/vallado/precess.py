# ----------------------------------------------------------------------------
#
#                           function precess
#
#  this function calulates the transformation matrix that accounts for the effects
#    of precession. both the 1980 and 2000 theories are handled. note that the 
#    required parameters differ a little. 
#
#  author        : david vallado                  719-573-2600   25 jun 2002
#
#  revisions
#    vallado     - consolidate with iau 2000                     14 feb 2005
#
#  inputs          description                    range / units
#    ttt         - julian centuries of tt
#    opt         - method option                  '01', '02', '96', '80'
#
#  outputs       :
#    prec        - transformation matrix for mod - j2000 (80 only)
#    psia        - cannonical precession angle    rad    (00 only)
#    wa          - cannonical precession angle    rad    (00 only)
#    ea          - cannonical precession angle    rad    (00 only)
#    xa          - cannonical precession angle    rad    (00 only)
#
#  locals        :
#    ttt2        - ttt squared
#    ttt3        - ttt cubed
#    zeta        - precession angle               rad
#    z           - precession angle               rad
#    theta       - precession angle               rad
#    oblo        - obliquity value at j2000 epoch "
#
#  coupling      :
#    none        -
#
#  references    :
#    vallado       2004, 214-216, 219-221
#
# [prec,psia,wa,ea,xa] = precess ( ttt, opt );
# ----------------------------------------------------------------------------

import numpy as np

def precess(ttt, opt):
    """
    Calculate the transformation matrix that accounts for the effects of precession.
    Both the 1980 and 2000 theories are handled. Note that the required parameters 
    differ a little.
    
    Args:
        ttt: julian centuries of tt
        opt: method option ('01', '02', '96', '80')
        
    Returns:
        prec: transformation matrix for mod - j2000 (80 only)
        psia: cannonical precession angle (rad) (00 only)
        wa: cannonical precession angle (rad) (00 only)
        ea: cannonical precession angle (rad) (00 only)
        xa: cannonical precession angle (rad) (00 only)
    """
    # TODO: Implement sethelp function
    # sethelp
    
    # " to rad
    convrt = np.pi / (180.0 * 3600.0)
    ttt2 = ttt * ttt
    ttt3 = ttt2 * ttt
    
    # ------------------- fk4 b1950 precession angles --------------------
    if opt == '50':
        # ---- Newcomb Exp Supp 61 approach, but see GTDS pg 3-17
        # Exp Supp 61 says use 1900? but gtds says use 1950. 
        # for these calls, ttt will come in with the current jd
        t1 = 0.0  # (ttt - 2415020.31352)/36524.2198782;  % set start as B1900, 0.0 to simplify
        t2 = (ttt - 2433282.42345905) / 36525  # uses B1950  
        ttt = t2 - t1
        ttt2 = ttt * ttt
        ttt3 = ttt * ttt2
        # exp supp 61 pg 38
        psia = 50.3708 + 0.0050 * ttt
        wa = 0.0  # not sure which one is which...
        ea = 84428.26 - 46.845 * ttt - 0.00059 * ttt2 + 0.00181 * ttt3
        xa = 0.1247 - 0.0188 * ttt
        print('50prec %15.9f' % ttt)
        # GTDS pg 3-17 using days from 1950 - avoids long precession constants...
        zeta = 2304.9969 * ttt + 0.302 * ttt2 + 0.01808 * ttt3  # "
        theta = 2004.2980 * ttt - 0.425936 * ttt2 - 0.0416 * ttt3
        z = 2304.9969 * ttt + 1.092999 * ttt2 + 0.0192 * ttt3
        
        # pass these back out for testing
        psia = zeta
        wa = theta
        ea = z
    # ------------------- iau 76 precession angles --------------------
    else:
        if opt == '80':
            psia = 5038.7784 * ttt - 1.07259 * ttt2 - 0.001147 * ttt3  # "
            wa = 84381.448 + 0.05127 * ttt2 - 0.007726 * ttt3
            ea = 84381.448 - 46.8150 * ttt - 0.00059 * ttt2 + 0.001813 * ttt3
            xa = 10.5526 * ttt - 2.38064 * ttt2 - 0.001125 * ttt3
            zeta = 2306.2181 * ttt + 0.30188 * ttt2 + 0.017998 * ttt3  # "
            theta = 2004.3109 * ttt - 0.42665 * ttt2 - 0.041833 * ttt3
            z = 2306.2181 * ttt + 1.09468 * ttt2 + 0.018203 * ttt3
        # ------------------ iau 03 precession angles -------------------
        else:
            oblo = 84381.406  # "
            psia = ((((-0.0000000951 * ttt + 0.000132851) * ttt - 0.00114045) * ttt - 1.0790069) * ttt + 5038.481507) * ttt  # "
            wa = ((((0.0000003337 * ttt - 0.000000467) * ttt - 0.00772503) * ttt + 0.0512623) * ttt - 0.025754) * ttt + oblo
            ea = ((((-0.0000000434 * ttt - 0.000000576) * ttt + 0.00200340) * ttt - 0.0001831) * ttt - 46.836769) * ttt + oblo
            xa = ((((-0.0000000560 * ttt + 0.000170663) * ttt - 0.00121197) * ttt - 2.3814292) * ttt + 10.556403) * ttt
            
            zeta = ((((-0.0000003173 * ttt - 0.000005971) * ttt + 0.01801828) * ttt + 0.2988499) * ttt + 2306.083227) * ttt + 2.650545  # "
            theta = ((((-0.0000001274 * ttt - 0.000007089) * ttt - 0.04182264) * ttt - 0.4294934) * ttt + 2004.191903) * ttt
            z = ((((0.0000002904 * ttt - 0.000028596) * ttt + 0.01826837) * ttt + 1.0927348) * ttt + 2306.077181) * ttt - 2.650545
    
    # convert units to rad
    psia = psia * convrt  # rad
    wa = wa * convrt
    ea = ea * convrt
    xa = xa * convrt
    zeta = zeta * convrt
    theta = theta * convrt
    z = z * convrt
    
    # TODO: Implement iauhelp variable
    iauhelp = 'n'  # placeholder
    
    if iauhelp == 'y':
        print('pr %11.7f  %11.7f  %11.7f %11.7fdeg' % (psia * 180 / np.pi, wa * 180 / np.pi, ea * 180 / np.pi, xa * 180 / np.pi))
        print('pr %11.7f  %11.7f  %11.7fdeg' % (zeta * 180 / np.pi, theta * 180 / np.pi, z * 180 / np.pi))
    
    if (opt == '80') or (opt == '50'):
        coszeta = np.cos(zeta)
        sinzeta = np.sin(zeta)
        costheta = np.cos(theta)
        sintheta = np.sin(theta)
        cosz = np.cos(z)
        sinz = np.sin(z)
        
        # ----------------- form matrix  mod to j2000 -----------------
        prec = np.zeros((3, 3))
        prec[0, 0] = coszeta * costheta * cosz - sinzeta * sinz
        prec[0, 1] = coszeta * costheta * sinz + sinzeta * cosz
        prec[0, 2] = coszeta * sintheta
        prec[1, 0] = -sinzeta * costheta * cosz - coszeta * sinz
        prec[1, 1] = -sinzeta * costheta * sinz + coszeta * cosz
        prec[1, 2] = -sinzeta * sintheta
        prec[2, 0] = -sintheta * cosz
        prec[2, 1] = -sintheta * sinz
        prec[2, 2] = costheta
        
        # ----------------- do rotations instead ----------------------
        # p1 = rot3mat(z)
        # p2 = rot2mat(-theta)
        # p3 = rot3mat(zeta)
        # prec = p3*p2*p1
    else:
        # TODO: Implement rot3mat and rot1mat functions
        # a4 = rot3mat(-xa)
        # a5 = rot1mat(wa)
        # a6 = rot3mat(psia)
        # a7 = rot1mat(-oblo)
        # prec = a7*a6*a5*a4
        
        # Placeholder - identity matrix
        prec = np.eye(3)
    
    return prec, psia, wa, ea, xa 