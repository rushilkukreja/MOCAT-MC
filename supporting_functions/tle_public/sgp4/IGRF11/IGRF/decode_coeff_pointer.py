def decode_coeff_pointer(np):
    """
    Decode IGRF11 coefficient pointer to extract year number and coefficient index.
    Parameters
    ----------
    np : int
        Pointer index (1-based)
    Returns
    -------
    nyear : int
        Year index
    ncoef : int
        Coefficient index
    """
    np1_max = 2280
    if np <= np1_max:
        nyear = np // 120 + 1
        ncoef = np - (nyear - 1) * 120
        if ncoef == 0:
            ncoef = 120
            nyear += 1
    elif np <= 3255:
        np2 = np - np1_max
        nyear = np2 // 195 + 1
        ncoef = np2 - (nyear - 1) * 195
        if ncoef == 0:
            ncoef = 195
            nyear += 1
        nyear = 19 + nyear
    else:
        raise ValueError('np > 3255!')
    return nyear, ncoef 