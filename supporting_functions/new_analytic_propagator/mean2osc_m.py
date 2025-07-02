import numpy as np

def mean2osc_m(x, param):
    """
    Convert mean orbital elements to osculating elements (single set, not vectorized).
    x: array-like, shape (6,)
        [a, e, inc, RAAN, arg_per, mean_anom]
    param: object with required attributes
    Returns:
        osc_orbital_elements: ndarray, shape (6,)
        theta_osc: float
    """
    e = x[1]
    Epw = x[5]
    Mo = Epw
    for _ in range(1000):
        DeltaEpw = -(Mo - Epw + e * np.sin(Epw)) / (-1 + e * np.cos(Epw))
        Epw = Epw + DeltaEpw
        if np.abs(DeltaEpw) < 1e-13:
            break
    E = Epw
    theta = 2 * np.arctan(np.sqrt((1 + e) / (1 - e)) * np.tan(E / 2))
    if e > 1:
        print('Warning: hyperbolic orbit in mean2osc_m')
        print(f'e: {e:.3e}\ttheta: {theta:.3e}')
    # mean2osc is assumed to be another function in this module
    from .mean2osc import mean2osc
    oeosc = mean2osc(np.concatenate([x[:5], [theta]]), param)
    theta_osc = oeosc[5]
    e_osc = oeosc[1]
    E_osc = 2 * np.arctan(np.power(np.sqrt((1 + e_osc) / (1 - e_osc)), -1) * np.tan(theta_osc / 2))
    M_osc = E_osc - e_osc * np.sin(E_osc)
    osc_orbital_elements = np.array([oeosc[0], oeosc[1], oeosc[2], oeosc[3], oeosc[4], M_osc])
    return osc_orbital_elements, theta_osc 