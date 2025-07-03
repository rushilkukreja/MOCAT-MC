import numpy as np

def rendz(rcs1, rcs3, phasei, einit, efinal, nuinit, nufinal, ktgt, kint):
    # This procedure calculates parameters for a hohmann transfer rendezvous.
    twopi = 2.0 * np.pi
    mu = 1.0  # canonical
    atrans = (rcs1 + rcs3) / 2.0
    dttutrans = np.pi * np.sqrt(atrans ** 3 / mu)
    angvelint = np.sqrt(mu / (rcs1 ** 3))
    angveltgt = np.sqrt(mu / (rcs3 ** 3))
    vint = np.sqrt(mu / rcs1)
    # Check for satellites in the same orbits
    if abs(angvelint - angveltgt) < 1e-6:
        periodtrans = (ktgt * twopi + phasei) / angveltgt
        atrans = (periodtrans / (twopi * kint)) ** (2.0 / 3.0)
        rp = 2.0 * atrans - rcs1
        if rp < 1.0:
            raise ValueError('error - the transfer orbit intersects the earth')
        vtrans = np.sqrt((2.0 * mu) / rcs1 - mu / atrans)
        deltav = 2.0 * (vtrans - vint)
        waittime = 0.0
        phasef = phasei
        waittime = periodtrans
        leadang = 0.0
    else:
        leadang = angveltgt * dttutrans
        phasef = leadang - np.pi
        waittime = (phasef - phasei + 2.0 * np.pi * ktgt) / (angvelint - angveltgt)
        a1 = (rcs1 * (1.0 + einit * np.cos(nuinit))) / (1.0 - einit ** 2)
        a2 = (rcs1 + rcs3) / 2.0
        a3 = (rcs3 * (1.0 + efinal * np.cos(nufinal))) / (1.0 - efinal ** 2)
        sme1 = -mu / (2.0 * a1)
        sme2 = -mu / (2.0 * a2)
        sme3 = -mu / (2.0 * a3)
        vinit = np.sqrt(2.0 * ((mu / rcs1) + sme1))
        vtransa = np.sqrt(2.0 * ((mu / rcs1) + sme2))
        deltava = abs(vtransa - vinit)
        vfinal = np.sqrt(2.0 * ((mu / rcs3) + sme3))
        vtransb = np.sqrt(2.0 * ((mu / rcs3) + sme2))
        deltavb = abs(vfinal - vtransb)
        deltav = deltava + deltavb
    return phasef, waittime, deltav 