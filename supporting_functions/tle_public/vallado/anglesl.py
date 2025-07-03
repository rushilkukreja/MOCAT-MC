"""
------------------------------------------------------------------------------

                           function [theta,theta1,theta2] = anglesl( r1,r2,r3 )

  this function finds the angles between three position vectors using the
    law of cosines.

  author        : david vallado                  719-573-2600   27 may 2002

  references    :
    vallado       2001, 246

[theta,theta1,theta2] = anglesl( r1,r2,r3 )
------------------------------------------------------------------------------
"""
import numpy as np

def anglesl(r1, r2, r3):
    def mag(v):
        return np.linalg.norm(v)
    # Compute the angles using the law of cosines
    cos_theta = np.dot(r1, r2) / (mag(r1) * mag(r2))
    cos_theta1 = np.dot(r2, r3) / (mag(r2) * mag(r3))
    cos_theta2 = np.dot(r1, r3) / (mag(r1) * mag(r3))
    theta = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    theta1 = np.arccos(np.clip(cos_theta1, -1.0, 1.0))
    theta2 = np.arccos(np.clip(cos_theta2, -1.0, 1.0))
    return theta, theta1, theta2 