# -----
#   vallado       2007, 370, alg 46, ex 6-10
# function [ttrans,tphase,dvphase,dvtrans1,dvtrans2,aphase ] = noncoplr(phasei,aint,atgt,ktgt,kint,arglatint,nodeint,truelon,deltai);
#------

import numpy as np

def noncoplr(phasei, aint, atgt, ktgt, kint, arglatint, nodeint, truelon, deltai):
    """
    Calculate non-coplanar orbital transfer parameters.
    
    Args:
        phasei: initial phase angle
        aint: initial semi-major axis
        atgt: target semi-major axis
        ktgt: target orbit number
        kint: initial orbit number
        arglatint: initial argument of latitude
        nodeint: initial node
        truelon: true longitude
        deltai: inclination change
        
    Returns:
        ttrans: transfer time
        tphase: phase time
        dvphase: phase delta v
        dvtrans1: first transfer delta v
        dvtrans2: second transfer delta v
        aphase: phase semi-major axis
    """
    twopi = 6.28318530717959
    rad = 57.29577951308230
    mu = 1.0  # canonical
    
    angvelint = np.sqrt(mu / (aint * aint * aint))
    angveltgt = np.sqrt(mu / (atgt * atgt * atgt))
    atrans = (aint + atgt) * 0.5
    ttrans = np.pi * np.sqrt((atrans * atrans * atrans) / mu)
    
    deltatnode = phasei / angvelint
    
    lead = angveltgt * ttrans
    
    omeganode = angveltgt * deltatnode
    
    phasenew = nodeint + np.pi - (truelon + omeganode)
    
    leadnew = np.pi + phasenew
    
    tphase = (leadnew - lead + twopi * ktgt) / angveltgt
    
    aphase = (mu * (tphase / (twopi * kint))**2)**(1.0 / 3.0)
    
    # -----------------  find deltav's  -----------------
    vint = np.sqrt(mu / aint)
    vphase = np.sqrt(2.0 * mu / aint - mu / aphase)
    dvphase = vphase - vint
    
    vtrans1 = np.sqrt(2.0 * mu / aint - mu / atrans)
    dvtrans1 = vtrans1 - vphase
    
    vtrans2 = np.sqrt(2.0 * mu / atgt - mu / atrans)
    vtgt = np.sqrt(mu / atgt)
    dvtrans2 = np.sqrt(vtgt * vtgt + vtrans2 * vtrans2 - 2.0 * vtgt * vtrans2 * np.cos(deltai))
    
    ttotal = deltatnode + ttrans + tphase
    
    return ttrans, tphase, dvphase, dvtrans1, dvtrans2, aphase 