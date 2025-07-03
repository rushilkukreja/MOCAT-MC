"""
------------------------------------------------------------------------------

                           function cubicspl1

  this function fits a cubic spline to a set of data points.

  author        : david vallado                  719-573-2600   27 may 2002

  references    :
    vallado       2001, 100-102

[coeffs] = cubicspl1(x, y)
------------------------------------------------------------------------------
"""
import numpy as np

def cubicspl1(x, y):
    # This is a simple cubic spline fit using numpy's polyfit for demonstration.
    # For a full spline, use scipy.interpolate.CubicSpline in practice.
    coeffs = np.polyfit(x, y, 3)
    return coeffs 