import numpy as np

def analytic_propagation_vec(input_oe, param):
    """
    Vectorized analytic propagation of near-circular satellite orbits in the atmosphere of an oblate planet.
    Reference: Martinusi et al., Celestial Mechanics and Dynamical Astronomy 123, no. 1 (2015): 85-103.
    input_oe: ndarray, shape (N,6)
    param: object with required attributes
    Returns:
        out_oe: ndarray, shape (N,6)
        errors: ndarray, shape (N,)
    """
    errors = np.zeros(input_oe.shape[0], dtype=int)
    re = param.req
    J2 = param.j2
    mu = param.mu
    a_0 = input_oe[:, 0]
    a_minus_re = a_0 - re
    if param.density_profile.lower() == 'jb2008':
        rho_0 = np.zeros_like(a_0)
        check_above = a_minus_re > param.alt[-1, 0]
        check_below = a_minus_re < param.alt[0, 0]
        check_in_range = ~check_above & ~check_below
        rho_0[check_in_range] = lininterp2_vec_v2(param.alt[:, 0], param.dens_times[0, :], param.dens_value, a_minus_re[check_in_range], param.jd) * 1e9
        rho_0[check_above] = lininterp1_vec(param.dens_times[0, :], param.dens_value[-1, :], param.jd) * 1e9
        rho_0[check_below] = lininterp1_vec(param.dens_times[0, :], param.dens_value[0, :], param.jd) * 1e9
    elif param.density_profile.lower() == 'static':
        rho_0 = densityexp_vec(a_minus_re) * 1e9
    else:
        rho_0 = np.full_like(a_0, 1e-20)
    C_0 = np.maximum((param.Bstar / (1e6 * 0.157)) * rho_0, 1e-20)
    k2_over_mu = J2 * re ** 2 / 2
    t = param.t
    t_0 = param.t_0
    e_0 = input_oe[:, 1]
    inc_0 = input_oe[:, 2]
    bigO_0 = input_oe[:, 3]
    omega_0 = input_oe[:, 4]
    Mo_0 = input_oe[:, 5]
    c = np.cos(inc_0)
    c_sq = c ** 2
    n_0 = np.sqrt(mu) * a_0 ** (-1.5)
    alpha0_sq = (e_0 / np.sqrt(a_0)) ** 2
    beta_0 = (np.sqrt(3) / 2) * e_0
    tan_atan_beta0 = np.maximum(np.tan(np.arctan(beta_0) - beta_0 * n_0 * a_0 * C_0 * (t - t_0)), 0)
    a = (a_0 / beta_0 ** 2) * tan_atan_beta0 ** 2
    e = (2 / np.sqrt(3)) * tan_atan_beta0
    check_beta = beta_0 == 0
    if np.any(check_beta):
        a0_beta = a_0[check_beta]
        a[check_beta] = a0_beta * (1 - C_0[check_beta] * n_0[check_beta] * a0_beta * (t - t_0))
    a_sq = a ** 2
    four_thirds_over_a_cb = 4 / 3 / (a_sq * a)
    a0_sq = a_0 ** 2
    four_thirds_over_a0_cb = 4 / 3 / (a0_sq * a_0)
    alpha0sq_over_asq = alpha0_sq / a_sq
    alpha0sq_over_a0sq = alpha0_sq / a0_sq
    Mo = (0.5 / a - 0.5 / a_0 + 3 / 8 * alpha0_sq * np.log(a / a_0)) / C_0 + 3 * k2_over_mu / 16 * (3 * c_sq - 1) * (1.5 * (alpha0sq_over_asq - alpha0sq_over_a0sq) + four_thirds_over_a_cb - four_thirds_over_a0_cb) / C_0 + Mo_0
    five_a0sq_over2_tau2_plus_4thirds_over_tau3_over_C0 = (2.5 * (alpha0sq_over_asq - alpha0sq_over_a0sq) + four_thirds_over_a_cb - four_thirds_over_a0_cb) / C_0
    omega = 3 * k2_over_mu / 16 * (5 * c_sq - 1) * five_a0sq_over2_tau2_plus_4thirds_over_tau3_over_C0 + omega_0
    bigO = -3 * k2_over_mu / 8 * c * five_a0sq_over2_tau2_plus_4thirds_over_tau3_over_C0 + bigO_0
    out_oe = np.column_stack([a, e, np.mod(inc_0, 2 * np.pi), np.mod(bigO, 2 * np.pi), np.mod(omega, 2 * np.pi), np.mod(Mo, 2 * np.pi)])
    not_real = ~np.isreal(inc_0) | ~np.isreal(bigO) | ~np.isreal(omega) | ~np.isreal(Mo)
    errors[not_real] = 1
    out_oe[not_real, :] = input_oe[not_real, :]
    return out_oe, errors

# Placeholders for lininterp1_vec, lininterp2_vec_v2, densityexp_vec
# These should be implemented or imported as needed. 