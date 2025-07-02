import numpy as np

def osc2mean_m_vec(x, param, theta_osc=None):
    """
    Vectorized conversion from osculating to mean elements.
    x: ndarray, shape (N,6)
    param: object with required attributes
    theta_osc: ndarray or None
    Returns:
        mean_orbital_elements: ndarray, shape (N,6)
        theta_mean: ndarray, shape (N,)
        E_mean: ndarray, shape (N,)
    """
    if theta_osc is None:
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
        theta_osc = 2 * np.arctan(sqrt_ep1_em1 * np.tan(Epw / 2))
    from .osc2mean_vec import osc2mean_vec
    oemean = osc2mean_vec(np.column_stack([x[:, :5], theta_osc]), param)
    theta_mean = oemean[:, 5]
    e_mean = oemean[:, 1]
    E_mean = 2 * np.arctan(np.power(np.sqrt((1 + e_mean) / (1 - e_mean)), -1) * np.tan(theta_mean / 2))
    M_mean = E_mean - e_mean * np.sin(E_mean)
    mean_orbital_elements = np.column_stack([oemean[:, :5], M_mean])
    return mean_orbital_elements, theta_mean, E_mean 