import numpy as np
import pandas as pd
import os

def GetIGRF11_Coefficients(output_matfile=None):
    """
    Get IGRF11 Coefficients from Excel file.
    Parameters
    ----------
    output_matfile : str or None
        If provided, saves the coefficients to a .npz file with this name.
    Returns
    -------
    gh : np.ndarray
        Array of coefficients
    date : list of str
        List of date strings
    """
    ff = 'igrf11coeffs.xls'
    if not os.path.exists(ff):
        raise FileNotFoundError(f"Excel file {ff} not found.")
    num = pd.read_excel(ff, header=None).values.T
    dd = num[2:, 0]
    ndate = len(dd)
    date = [str(dd[n]) for n in range(ndate-1)]
    date.append('2010-15')
    num = num[2:, 1:]
    gh = np.full((3255,), np.nan)
    for n in range(19):
        n1 = n * 120
        n2 = (n + 1) * 120
        gh[n1:n2] = num[n, :120]
    for n in range(19, 24):
        n11 = n2 + (n - 19) * 195
        n22 = n2 + (n - 18) * 195
        gh[n11:n22] = num[n, :195]
    if output_matfile:
        np.savez(output_matfile, gh=gh)
    return gh, date 