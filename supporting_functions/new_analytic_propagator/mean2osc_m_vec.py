import numpy as np

def mean2osc_m_vec(x, param):
    """
    Vectorized conversion from mean to osculating elements.
    x: ndarray, shape (N,6)
    param: object with required attributes
    Returns:
        osc_orbital_elements: ndarray, shape (N,6)
        theta_osc: ndarray, shape (N,)
        E_osc: ndarray, shape (N,)
    """
    e = x[:, 1]
    Epw = x[:, 5].copy()
    Mo = Epw.copy()
    check_mag = np.arange(Epw.size)
    for _ in range(1000):
        Epw_check = Epw[check_mag]
        e_check = e[check_mag]
        DeltaEpw = -(Mo[check_mag] - Epw_check + e_check * np.sin(Epw_check)) / (-1 + e_check * np.cos(Epw_check))
        Epw[check_mag] = Epw_check + DeltaEpw
        check_mag = check_mag[DeltaEpw > 1e-13]
        if check_mag.size == 0:
            break
    sqrt_ep1_em1 = np.sqrt((1 + e) / (1 - e))
    theta = 2 * np.arctan(sqrt_ep1_em1 * np.tan(Epw / 2))
    from .mean2osc_vec import mean2osc_vec
    oeosc = mean2osc_vec(np.column_stack([x[:, :5], theta]), param)
    theta_osc = oeosc[:, 5]
    e_osc = oeosc[:, 1]
    E_osc = 2 * np.arctan(np.power(np.sqrt((1 + e_osc) / (1 - e_osc)), -1) * np.tan(theta_osc / 2))
    M_osc = E_osc - e_osc * np.sin(E_osc)
    osc_orbital_elements = np.column_stack([oeosc[:, :5], M_osc])
    return osc_orbital_elements, theta_osc, E_osc 