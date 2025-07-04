"""
-----------------------------------------------------------------------------

    ionlychg.py

    This procedure calculates the delta v's for a change in inclination only.

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        deltai     - change in inclination          rad
        vinit      - initial velocity vector        er/tu
        fpa        - flight path angle              rad

    Outputs:
        deltavionly - answer

    References:
        Vallado 2007, 346, alg 39, ex 6-4
-----------------------------------------------------------------------------
"""
import numpy as np

def ionlychg(deltai, vinit, fpa):
    deltavionly = 2.0 * vinit * np.cos(fpa) * np.sin(0.5 * deltai)
    
    return deltavionly 