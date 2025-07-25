# ------------------------------------------------------------------------------
#
#                           function quartic
#
#  this function solves for the four roots of a quartic equation.  there are
#    no restrictions on the coefficients, and imaginary results are passed
#    out as separate values.  the general form is y = ax4 + bx3 + cx2 + dx + e.
#
#  author        : david vallado                  719-573-2600    1 mar 2001
#
#  revisions
#    vallado     - convert to matlab              719-573-2600   18 dec 2002
#
#  inputs          description                    range / units
#    a           - coeficient of x fourth term
#    b           - coefficient of x cubed term
#    c           - coefficient of x squared term
#    d           - coefficient of x term
#    e           - constant
#    opt         - option for output              I all roots including imaginary
#                                                 R only real roots
#                                                 U only unique real roots (no repeated)
#
#  outputs       :
#    r1r         - real portion of root 1
#    r1i         - imaginary portion of root 1
#    r2r         - real portion of root 2
#    r2i         - imaginary portion of root 2
#    r3r         - real portion of root 3
#    r3i         - imaginary portion of root 3
#    r4r         - real portion of root 4
#    r4i         - imaginary portion of root 4
#
#  locals        :
#    temp1       - temporary value
#    temp2       - temporary value
#    s           - alternate variable
#    h           - temporary value
#    hsqr        - h squared
#    hcube       - h cubed
#    p           - term in auxillary equation
#    q           - term in auxillary equation
#    r           - term in auxillary equation
#    delta       - discriminator for use with cardans formula
#    e0          - angle holder for trigonometric solution
#    phi         - angle used in trigonometric solution
#    cosphi      - cosine of phi
#    sinphi      - sine of phi
#    rprime      - values of roots before final work
#    temp        - temporary variable in finding max rprime
#    eta         - constant coefficient in quadric solutions
#    beta        - constant coefficient in quadric solutions
#
#  coupling      :
#    quadric     find roots of a quadric polynomial
#
#  references    :
#    vallado       2007, 976
#
# [r1r,r1i,r2r,r2i,r3r,r3i,r4r,r4i] = quartic( a,b,c,d,e,opt );
# ------------------------------------------------------------------------------

import numpy as np

def quartic(a, b, c, d, e, opt):
    """
    Solve for the four roots of a quartic equation. There are no restrictions 
    on the coefficients, and imaginary results are passed out as separate values. 
    The general form is y = ax^4 + bx^3 + cx^2 + dx + e.
    
    Args:
        a: coefficient of x fourth term
        b: coefficient of x cubed term
        c: coefficient of x squared term
        d: coefficient of x term
        e: constant
        opt: option for output ('I' all roots including imaginary, 
             'R' only real roots, 'U' only unique real roots (no repeated))
        
    Returns:
        r1r, r1i, r2r, r2i, r3r, r3i, r4r, r4i: real and imaginary parts of the four roots
    """
    # --------------------  implementation   ----------------------
    rad = 180.0 / np.pi
    onethird = 1.0 / 3.0
    small = 0.00000001
    r1r = 0.0
    r1i = 0.0
    r2r = 0.0
    r2i = 0.0
    r3r = 0.0
    r3i = 0.0
    r4r = 0.0
    r4i = 0.0
    root1 = 0.0
    root2 = 0.0
    root3 = 0.0
    
    if abs(a) > small:
        # ----------- force coefficients into std form ----------------
        b = b / a
        c = c / a
        d = d / a
        e = e / a
        
        h = -b / 4
        hsqr = h**2
        hcube = hsqr * h
        
        p = 6.0 * hsqr + 3.0 * b * h + c
        q = 4.0 * hcube + 3.0 * b * hsqr + 2.0 * c * h + d
        r = h * hcube + b * hcube + c * hsqr + d * h + e
        
        a = onethird * (-p * p - 12.0 * r)
        b = (1.0 / 27.0) * (-2.0 * p * p * p + 72.0 * p * r - 27.0 * q * q)
        s = -2.0 * onethird * p
        
        delta = (a * a * a / 27.0) + (b * b * 0.25)
        
        if abs(q) > small:
            # ------------------ use cardans formula ------------------
            if delta > small:
                temp1 = (-b * 0.5) + np.sqrt(delta)
                temp2 = (-b * 0.5) - np.sqrt(delta)
                temp1 = np.sign(temp1) * abs(temp1)**onethird
                temp2 = np.sign(temp2) * abs(temp2)**onethird
                root1 = temp1 + temp2
                
                root2 = -0.5 * (temp1 + temp2)
                r2i = -0.5 * np.sqrt(3.0) * (temp1 - temp2)
                root3 = -0.5 * (temp1 + temp2)
                r3i = -r2i
            else:
                # --------------- evaluate zero point -----------------
                if abs(delta) < small:
                    root1 = -2.0 * np.sign(b) * abs(b * 0.5)**onethird
                    root2 = np.sign(b) * abs(b * 0.5)**onethird
                    root3 = root2
                else:
                    # ------------ use trigonometric identities -------
                    e0 = 2.0 * np.sqrt(-a * onethird)
                    cosphi = (-b / (2.0 * np.sqrt(-a * a * a / 27.0)))
                    sinphi = np.sqrt(1.0 - cosphi * cosphi)
                    phi = np.arctan2(sinphi, cosphi)
                    if phi < 0.0:
                        phi = phi + 2 * np.pi
                    root1 = e0 * np.cos(phi * onethird)
                    root2 = e0 * np.cos(phi * onethird + 120.0 / rad)
                    root3 = e0 * np.cos(phi * onethird + 240.0 / rad)
            
            # --------------- find largest value of root -------------
            rprime = root1 + s
            if (rprime < root2 + s) and (abs(r2i) < 0.0001):
                rprime = root2 + s
            if (rprime < root3 + s) and (abs(r3i) < 0.0001):
                rprime = root3 + s
            
            # -- evaluate coefficients of two resulting quadratics ---
            if rprime > small:
                eta = 0.5 * (p + rprime - q / np.sqrt(rprime))
                beta = 0.5 * (p + rprime + q / np.sqrt(rprime))
            else:
                eta = 0.5 * p
                beta = 0.5 * p
                if rprime < 0.0:
                    rprime = -rprime
            
            # TODO: Implement quadric function
            # [r1r, r1i, r2r, r2i] = quadric(1.0, np.sqrt(rprime), eta, opt)
            # [r3r, r3i, r4r, r4i] = quadric(1.0, -np.sqrt(rprime), beta, opt)
            
            # Placeholder for quadric results
            r1r, r1i, r2r, r2i = 0.0, 0.0, 0.0, 0.0
            r3r, r3i, r4r, r4i = 0.0, 0.0, 0.0, 0.0
        else:
            # ------ case where solution reduces to a quadratic ------
            # TODO: Implement quadric function
            # [r1r, r1i, r3r, r3i] = quadric(1.0, p, r, opt)
            
            # Placeholder for quadric results
            r1r, r1i, r3r, r3i = 0.0, 0.0, 0.0, 0.0
            
            r = np.sqrt(r1r * r1r + r1i * r1i)
            phi = np.arctan2(r1i, r1r)
            if phi < 0.0:
                phi = phi + 2 * np.pi
            r1r = np.sqrt(r) * np.cos(phi * 0.5)
            r1i = np.sqrt(r) * np.sin(phi * 0.5)
            if r1i > 0.0:
                r2r = r1r
            else:
                r2r = -r1r
            r2i = -r1i
            
            r = np.sqrt(r3r * r3r + r3i * r3i)
            phi = np.arctan2(r3i, r3r)
            if phi < 0.0:
                phi = phi + 2 * np.pi
            r3r = np.sqrt(r) * np.cos(phi * 0.5)
            r3i = np.sqrt(r) * np.sin(phi * 0.5)
            if r3i > 0.0:
                r4r = r3r
            else:
                r4r = -r3r
            r4i = -r3i
    
    r1r = r1r + h
    r2r = r2r + h
    r3r = r3r + h
    r4r = r4r + h
    
    if opt == 'R':
        # TODO: Implement real root filtering
        pass
    
    return r1r, r1i, r2r, r2i, r3r, r3i, r4r, r4i 