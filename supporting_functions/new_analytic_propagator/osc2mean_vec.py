import numpy as np

def osc2mean_vec(oeosc, param):
    """
    Convert osculating classical orbital elements to mean classical orbital elements.

    Parameters
    ----------
    oeosc : ndarray
        Osculating orbital elements (Nx6 array):
            0: semimajor axis (km)
            1: eccentricity
            2: inclination (rad)
            3: RAAN (rad)
            4: argument of perigee (rad)
            5: true anomaly (rad)
    param : object
        Must have attributes req, j2

    Returns
    -------
    oemean : ndarray
        Mean orbital elements (Nx6 array)
    """
    req = param.req
    j2 = param.j2
    pi2 = 2.0 * np.pi

    eos = oeosc[:, 1]
    M = oeosc[:, 5]
    a = np.sin(M) * np.sqrt(1.0 - eos**2)
    b = eos + np.cos(M)
    eanom = np.arctan2(a, b)

    aos = oeosc[:, 0]
    ios = oeosc[:, 2]
    ranos = oeosc[:, 3]
    apos = oeosc[:, 4]
    si2 = np.sin(ios)**2
    maos = np.mod(eanom - eos * np.sin(eanom), pi2)
    aa = 1.0/3.0 - 0.5 * si2
    bb = 0.5 * si2

    check_e = eos < 0.01
    find_e = np.where(check_e)[0]
    find_note = np.where(~check_e)[0]

    # For eos < 0.01
    aos_e = aos[find_e]
    eos_e = eos[find_e]
    ios_e = ios[find_e]
    ranos_e = ranos[find_e]
    apos_e = apos[find_e]
    maos_e = maos[find_e]
    bb_e = bb[find_e]
    lamos = np.mod(maos_e + apos_e, pi2)
    zos = eos_e * np.cos(apos_e)
    etaos = eos_e * np.sin(apos_e)
    sl = np.sin(lamos)
    cl = np.cos(lamos)
    s2l = np.sin(2 * lamos)
    c2l = np.cos(2 * lamos)
    s3l = np.sin(3 * lamos)
    c3l = np.cos(3 * lamos)
    s2i = np.sin(2 * ios_e)
    am_e = aos_e.copy()
    lamm = lamos.copy()
    zm = zos.copy()
    etam = etaos.copy()
    threej2req2 = 3 * j2 * req * req
    for _ in range(5):
        asp_e = threej2req2 / am_e * (bb_e * c2l + (1 - 3.5 * bb_e) * zm * cl + (1 - 2.5 * bb_e) * etam * sl + 3.5 * bb_e * (zm * c3l + etam * s3l))
        am_e = aos_e - asp_e
        am2_e = am_e**2
        threej2req2_over2_am2 = threej2req2 / 2 / am2_e
        isp_e = threej2req2_over2_am2 / 4 * s2i * (c2l - zm * cl + etam * sl + 7/3 * (zm * c3l + etam * s3l))
        im_e = ios_e - isp_e
        ci = np.cos(im_e)
        s2i = np.sin(2 * im_e)
        bb_e = 0.5 * np.sin(im_e)**2
        ransp_e = threej2req2_over2_am2 * ci * (0.5 * s2l - 3.5 * zm * sl + 2.5 * etam * cl + 7/6 * (zm * s3l - etam * c3l))
        ranm_e = ranos_e - ransp_e
        lamsp = threej2req2_over2_am2 * (-0.5 * (1 - 5 * bb_e) * s2l + (7 - 77/4 * bb_e) * zm * sl - (6 - 55/4 * bb_e) * etam * cl - (7/6 - 77/12 * bb_e) * (zm * s3l - etam * c3l))
        lamm = lamos - lamsp
        sl = np.sin(lamm)
        cl = np.cos(lamm)
        s2l = np.sin(2 * lamm)
        c2l = np.cos(2 * lamm)
        s3l = np.sin(3 * lamm)
        c3l = np.cos(3 * lamm)
        s4l = np.sin(4 * lamm)
        c4l = np.cos(4 * lamm)
        zsp = threej2req2_over2_am2 * ((1 - 2.5 * bb_e) * cl + 7/6 * bb_e * c3l + (1.5 - 5 * bb_e) * zm * c2l + (2 - 3 * bb_e) * etam * s2l + 17/4 * bb_e * (zm * c4l + etam * s4l))
        zm = zos - zsp
        etasp = threej2req2_over2_am2 * ((1 - 3.5 * bb_e) * sl + 7/6 * bb_e * s3l + (1 - 6 * bb_e) * zm * s2l - (1.5 - 4 * bb_e) * etam * c2l + 17/4 * bb_e * (zm * s4l - etam * c4l))
        etam = etaos - etasp
    em_e = np.sqrt(etam**2 + zm**2)
    apm_e = np.zeros_like(em_e)
    check_em = em_e > 1.0e-8
    apm_e[check_em] = np.arctan2(etam[check_em], zm[check_em])
    mam_e = np.mod(lamm - apm_e, pi2)
    # For eos >= 0.01
    aos_note = aos[find_note]
    eos_note = eos[find_note]
    ios_note = ios[find_note]
    apos_note = apos[find_note]
    ranos_note = ranos[find_note]
    maos_note = maos[find_note]
    am_note = aos_note.copy()
    em_note = eos_note.copy()
    em_note2 = em_note**2
    one_minus_emnote = 1 - em_note2
    pm_note = aos_note * one_minus_emnote
    im_note = ios_note.copy()
    apm_note = apos_note.copy()
    mam_note = maos_note.copy()
    aa_note = aa[~check_e]
    bb_note = bb[~check_e]
    n_sats = em_note.size
    # Placeholder for kepler1_C_tanom/kepler1_vec_tanom
    tam_note = np.zeros_like(mam_note)  # TODO: Replace with actual anomaly solver
    um = np.mod(apm_note + tam_note, pi2)
    hm = pm_note / (1 + em_note * np.cos(tam_note))
    for _ in range(5):
        cos2um = np.cos(2 * um)
        sin2um = np.sin(2 * um)
        asp_note = threej2req2 / am_note * ((am_note / hm)**3 * (aa_note + bb_note * cos2um) - aa_note * one_minus_emnote**(-1.5))
        am_note = aos_note - asp_note
        isp_note = threej2req2 / 8 / pm_note**2 * np.sin(2 * im_note) * (cos2um + em_note * np.cos(tam_note + 2 * apm_note) + 1/3 * em_note * np.cos(3 * tam_note + 2 * apm_note))
        im_note = ios_note - isp_note
        si2_enote = np.sin(im_note)**2
        aa_note = 1/3 - 0.5 * si2_enote
        bb_note = 0.5 * si2_enote
        esp_note = threej2req2 / 2 / am_note**2 * (one_minus_emnote / em_note * ((am_note / hm)**3 * (aa_note + bb_note * cos2um) - aa_note * one_minus_emnote**(-1.5)) - bb_note / (em_note * one_minus_emnote) * (cos2um + em_note * np.cos(tam_note + 2 * apm_note) + em_note * np.cos(3 * tam_note + 2 * apm_note) / 3))
        em_note = eos_note - esp_note
        em_note2 = em_note**2
        one_minus_emnote = 1 - em_note2
        pm_note = am_note * one_minus_emnote
        hm = pm_note / (1.0 + em_note * np.cos(tam_note))
        tam_note = np.mod(tam_note, pi2)
        mam_note = np.mod(mam_note, pi2)
        eqoc = np.zeros_like(mam_note)
        check_tam = (np.abs(tam_note - np.pi) <= 1.0e-06) | (np.abs(mam_note - np.pi) <= 1.0e-06) | (np.abs(tam_note) <= 1.0e-06) | (np.abs(mam_note) <= 1.0e-06)
        eqoc[~check_tam] = tam_note[~check_tam] - mam_note[~check_tam]
        threej2req2_over2pm2 = threej2req2 / 2 / pm_note**2
        ransp_note = -threej2req2_over2pm2 * np.cos(im_note) * (eqoc + em_note * np.sin(tam_note) - 0.5 * sin2um - 0.5 * em_note * np.sin(tam_note + 2 * apm_note) - 1/6 * em_note * np.sin(3 * tam_note + 2 * apm_note))
        ranm_note = ranos_note - ransp_note
        apsp = threej2req2_over2pm2 * ((2 - 5 * bb_note) * (eqoc + em_note * np.sin(tam_note)) + (1 - 3 * bb_note) * ((1 - 0.25 * em_note2) * np.sin(tam_note) / em_note + 0.5 * np.sin(2 * tam_note) + em_note * np.sin(3 * tam_note + 2 * apm_note) / 12) - (0.5 * bb_note + (0.5 - 15/8 * bb_note) * em_note2) / em_note * np.sin(tam_note + 2 * apm_note) + em_note / 8 * bb_note * np.sin(tam_note - 2 * apm_note) - 0.5 * (1 - 5 * bb_note) * sin2um + (7/6 * bb_note - 1/6 * em_note2 * (1 - 19/4 * bb_note)) / em_note * np.sin(3 * tam_note + 2 * apm_note) + 0.75 * bb_note * np.sin(4 * tam_note + 2 * apm_note) + em_note / 8 * bb_note * np.sin(5 * tam_note + 2 * apm_note))
        apm_note = apos_note - apsp
        masp = threej2req2_over2pm2 * np.sqrt(one_minus_emnote) / em_note * (-(1 - 3 * bb_note) * ((1 - em_note2 / 4) * np.sin(tam_note) + em_note / 2 * np.sin(2 * tam_note) + em_note2 / 12 * np.sin(3 * tam_note)) + bb_note * (0.5 * (1 + 1.25 * em_note2) * np.sin(tam_note + 2 * apm_note) - em_note2 / 8 * np.sin(tam_note - 2 * apm_note) - 7/6 * (1 - em_note2 / 28) * np.sin(3 * tam_note + 2 * apm_note) - 0.75 * em_note * np.sin(4 * tam_note + 2 * apm_note) - em_note2 / 8 * np.sin(5 * tam_note + 2 * apm_note)))
        mam_note = maos_note - masp
        n_sats = em_note.size
        # Placeholder for kepler1_C_tanom/kepler1_vec_tanom
        tam_note = np.zeros_like(mam_note)  # TODO: Replace with actual anomaly solver
        um = np.mod(apm_note + tam_note, pi2)
    oemean = np.zeros((oeosc.shape[0], 6))
    em = np.concatenate([em_e, em_note])
    mod_mam = np.mod(np.concatenate([mam_e, mam_note]), pi2)
    n_sats = em.size
    # Placeholder for kepler1_C_tanom/kepler1_vec_tanom
    tanom = np.zeros_like(mod_mam)  # TODO: Replace with actual anomaly solver
    idx = np.concatenate([find_e, find_note])
    oemean[idx, :] = np.column_stack([
        np.concatenate([am_e, am_note]),
        em,
        np.concatenate([im_e, im_note]),
        np.concatenate([ranm_e, ranm_note]),
        np.concatenate([apm_e, apm_note]),
        tanom
    ])
    return oemean 