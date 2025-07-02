import numpy as np

def tod2eci(rtod, vtod, atod, ttt, ddpsi, ddeps):
    """
    Transforms a vector from the true equator true equinox frame of date (tod),
    to the mean equator mean equinox (j2000) frame.
    """
    # Placeholder functions
    def precess(ttt, mode):
        return np.eye(3), None, None, None, None
    def nutation(ttt, ddpsi, ddeps):
        return None, None, None, None, np.eye(3)
    prec, *_ = precess(ttt, '80')
    _, _, _, _, nut = nutation(ttt, ddpsi, ddeps)
    reci = prec @ nut @ rtod
    veci = prec @ nut @ vtod
    aeci = prec @ nut @ atod
    return reci, veci, aeci 