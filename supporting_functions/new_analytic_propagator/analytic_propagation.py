import numpy as np

def analytic_propagation(input_oe, param):
    """
    Analytic propagation of near-circular satellite orbits in the atmosphere of an oblate planet.
    Reference: Martinusi et al., Celestial Mechanics and Dynamical Astronomy 123, no. 1 (2015): 85-103.
    input_oe: array-like, shape (6,)
    param: object with required attributes
    Returns:
        out_oe: ndarray, shape (6,)
        error: int (0 if success, 1 if fallback to input)
    """
    error = 0
    re = param.req
    J2 = param.j2
    mu = param.mu
    # Density profile handling
    if param.density_profile.lower() == 'jb2008':
        alt = input_oe[0] - re
        if 200 < alt < 2000:
            rho_0 = lininterp2(param.alt[:, 0], param.dens_times[0, :], param.dens_value, alt, param.jd) * 1e9
        elif alt > 1100:
            rho_0 = lininterp1(param.dens_times[0, :], param.dens_value[-1, :], param.jd) * 1e9
        else:
            rho_0 = lininterp1(param.dens_times[0, :], param.dens_value[0, :], param.jd) * 1e9
    elif param.density_profile.lower() == 'static':
        rho_0 = densityexp(input_oe[0] - re) * 1e9
    else:
        rho_0 = 1e-16
    C_0 = max((abs(param.Bstar) / (1e6 * 0.157)) * rho_0, 1e-16)
    k2 = mu * J2 * re ** 2 / 2
    t = param.t
    t_0 = param.t_0
    a_0, e_0, inc_0, bigO_0, omega_0, Mo_0 = input_oe
    c = np.cos(inc_0)
    n_0 = np.sqrt(mu) * a_0 ** (-1.5)
    alpha_0 = e_0 / np.sqrt(a_0)
    beta_0 = (np.sqrt(3) / 2) * e_0
    tan_coeff = max(np.tan(np.arctan(beta_0) - beta_0 * n_0 * a_0 * C_0 * (t - t_0)), 0)
    a = (a_0 / beta_0 ** 2) * tan_coeff ** 2
    e = (1 / (np.sqrt(3) / 2)) * tan_coeff
    Mo = (1 / 8) * (1 / C_0) * (4 / a + 3 * alpha_0 ** 2 * np.log(a / a_0)) - (1 / 8) * (1 / C_0) * (4 / a_0 + 3 * alpha_0 ** 2 * np.log(a_0 / a_0)) + (3 * k2 * (3 * c ** 2 - 1)) / (16 * mu) * (1 / C_0) * ((3 * alpha_0 ** 2 / 2) * 1 / a ** 2 + 4 / (3 * a ** 3)) - (3 * k2 * (3 * c ** 2 - 1)) / (16 * mu) * (1 / C_0) * ((3 * alpha_0 ** 2 / 2) * 1 / a_0 ** 2 + 4 / (3 * a_0 ** 3)) + Mo_0
    omega = (3 * k2 * (5 * c ** 2 - 1)) / (16 * mu) * (1 / C_0) * ((5 * alpha_0 ** 2 / 2) * 1 / a ** 2 + 4 / (3 * a ** 3)) - (3 * k2 * (5 * c ** 2 - 1)) / (16 * mu) * (1 / C_0) * ((5 * alpha_0 ** 2 / 2) * 1 / a_0 ** 2 + 4 / (3 * a_0 ** 3)) + omega_0
    bigO = -(3 * k2 * c) / (8 * mu) * (1 / C_0) * ((5 * alpha_0 ** 2 / 2) * 1 / a ** 2 + 4 / (3 * a ** 3)) + (3 * k2 * c) / (8 * mu) * (1 / C_0) * ((5 * alpha_0 ** 2 / 2) * 1 / a_0 ** 2 + 4 / (3 * a_0 ** 3)) + bigO_0
    if all(map(np.isreal, [inc_0, bigO, omega, Mo])):
        out_oe = np.array([a, e, np.mod(inc_0, 2 * np.pi), np.mod(bigO, 2 * np.pi), np.mod(omega, 2 * np.pi), np.mod(Mo, 2 * np.pi)])
    else:
        out_oe = np.array(input_oe)
        error = 1
    return out_oe, error

# Placeholders for lininterp1, lininterp2, densityexp
# These should be implemented or imported as needed. 