# ------------------------------------------------------------------------------
#
#                           function light
#
#  this function determines if a spacecraft is sunlit or in the dark at a
#    particular time.  an oblate earth and cylindrical shadow is assumed.
#
#  author        : david vallado                  719-573-2600   27 may 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    r           - position vector of sat         er
#    jd          - julian date at desired time    days from 4713 bc
#    whichkind   - spherical or ellipsoidal earth 's', 'e'*default
#
#  outputs       :
#    vis         - visibility flag                'yes','no '
#
#  locals        :
#    rtasc       - suns right ascension           rad
#    decl        - suns declination               rad
#    rsun        - sun vector                     au
#    auer        - conversion from au to er
#
#  coupling      :
#    sun         - position vector of sun
#    lncom1      - multiple a vector by a constant
#    sight       - does line-of-sight exist beteen vectors
#
#  references    :
#    vallado       2001, 291-295, alg 35, ex 5-6
#
# [lit] = light ( r, jd, whichkind );
# ------------------------------------------------------------------------------

def light(r, jd, whichkind='e'):
    """
    Determine if a spacecraft is sunlit or in the dark at a particular time.
    An oblate earth and cylindrical shadow is assumed.
    
    Args:
        r: position vector of satellite (er)
        jd: julian date at desired time (days from 4713 bc)
        whichkind: spherical or ellipsoidal earth ('s', 'e'*default)
        
    Returns:
        lit: visibility flag ('yes', 'no')
    """
    auer = 149597870.0 / 6378.1363
    
    # -------------------------  implementation   -------------------------
    # TODO: Implement sun function
    # [rsun, rtasc, decl] = sun(jd)
    rsun = None  # Placeholder for sun function
    rtasc = None
    decl = None
    
    if rsun is not None:
        rsun = auer * rsun
        
        # ------------ is the satellite in the shadow? ----------------
        # TODO: Implement sight function
        # [lit] = sight(rsun, r, whichkind)
        lit = None  # Placeholder for sight function
    else:
        lit = None
    
    return lit 