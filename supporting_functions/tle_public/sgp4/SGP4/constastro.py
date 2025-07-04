import numpy as np

def constastro():
    """
    Define astronomical constants for satellite orbit calculations.
    
    Returns:
    --------
    constants : dict
        Dictionary containing astronomical constants
    """
    # Define basic constants first
    ae = 1.0e0  # Earth's radius in earth radii
    f = 3.35281066474748e-3  # Earth's flattening
    ck2 = 5.413080e-4  # 0.5 * J2 * AE²
    ck4 = 0.62098875e-6  # -0.375 * J4 * AE⁴
    u0 = ae * f * f  # AE * f²
    
    constants = {
        'tumin': 1.0 / 13.4468396969593e0,  # minutes in one time unit
        'mu': 398600.4418e0,                 # Earth's gravitational parameter (km³/s²)
        'radiusearthkm': 6378.135e0,         # Earth's radius (km)
        'xke': 0.0743669161331734132e0,      # sqrt(mu) in earth radii^1.5/min
        'j2': 0.001082616e0,                 # J2 harmonic
        'j3': -0.00000253881e0,              # J3 harmonic
        'j4': -0.00000165597e0,              # J4 harmonic
        'j3oj2': -0.00000253881e0 / 0.001082616e0,  # J3/J2
        'ae': ae,                            # Earth's radius in earth radii
        'de2ra': np.pi / 180.0e0,            # Degrees to radians
        'pi': np.pi,                         # Pi
        'pio2': np.pi / 2.0e0,               # Pi/2
        'twopi': 2.0e0 * np.pi,              # 2*Pi
        'e6a': 1.0e-6,                       # 1.0e-6
        'qoms2t': 1.88027915901527064352e-9, # (QO - mS)² in earth radii⁴
        's': 1.012229280189271e0,            # SGP4 density function parameter
        'vkmper': 7.905365719e0,             # Velocity in km/s
        'minsperday': 1440.0e0,              # Minutes per day
        'secday': 86400.0e0,                 # Seconds per day
        'omegaearth': 1.00273790934e0,       # Earth's rotation rate (revs/day)
        'f': f,                              # Earth's flattening
        'rf': 298.257223563e0,               # Earth's reciprocal flattening
        'gstime': 0.0e0,                     # Greenwich sidereal time
        'x2o3': 2.0e0 / 3.0e0,               # 2/3
        'ck2': ck2,                          # 0.5 * J2 * AE²
        'ck4': ck4,                          # -0.375 * J4 * AE⁴
        'a3ovk2': -1.0e0 / (ck2 * ae**2),    # -AE² / CK2
        'x1mth2': 1.0e0 - f**2,              # 1 - f²
        'c1sq': ae**4 * ck2**2,              # AE⁴ * CK2²
        'd2': 4.0e0 * ae * ck2,              # 4 * AE * CK2
        'd3': 4.0e0 * ck4,                   # 4 * CK4
        'd4': 4.0e0 * ck4 / ae,              # 4 * CK4 / AE
        't2cof': 1.0e0 - 2.0e0 * ck2 * ae**2,  # 1 - 2*CK2*AE²
        'xlcof': 0.125e0 * ck2 * ae**2,      # 0.125 * CK2 * AE²
        'aycof': 0.25e0 * ck2 * ae**2,       # 0.25 * CK2 * AE²
        'xl': ae + ae * f,                   # AE + AE*f
        'betal': np.sqrt(1.0e0 - f**2),      # sqrt(1 - f²)
        'u0': u0,                            # AE * f²
        'u02': u0**2,                        # U0²
        'u04': u0**4,                        # U0⁴
        'u06': u0**6,                        # U0⁶
        'u08': u0**8,                        # U0⁸
        'u10': u0**10,                       # U0¹⁰
        'u12': u0**12,                       # U0¹²
        'u14': u0**14,                       # U0¹⁴
        'u16': u0**16,                       # U0¹⁶
        'u18': u0**18,                       # U0¹⁸
        'u20': u0**20,                       # U0²⁰
        'u22': u0**22,                       # U0²²
        'u24': u0**24,                       # U0²⁴
        'u26': u0**26,                       # U0²⁶
        'u28': u0**28,                       # U0²⁸
        'u30': u0**30,                       # U0³⁰
        'u32': u0**32,                       # U0³²
        'u34': u0**34,                       # U0³⁴
        'u36': u0**36,                       # U0³⁶
        'u38': u0**38,                       # U0³⁸
        'u40': u0**40,                       # U0⁴⁰
        'u42': u0**42,                       # U0⁴²
        'u44': u0**44,                       # U0⁴⁴
        'u46': u0**46,                       # U0⁴⁶
        'u48': u0**48,                       # U0⁴⁸
        'u50': u0**50,                       # U0⁵⁰
        'u52': u0**52,                       # U0⁵²
        'u54': u0**54,                       # U0⁵⁴
        'u56': u0**56,                       # U0⁵⁶
        'u58': u0**58,                       # U0⁵⁸
        'u60': u0**60,                       # U0⁶⁰
        'u62': u0**62,                       # U0⁶²
        'u64': u0**64,                       # U0⁶⁴
        'u66': u0**66,                       # U0⁶⁶
        'u68': u0**68,                       # U0⁶⁸
        'u70': u0**70,                       # U0⁷⁰
        'u72': u0**72,                       # U0⁷²
        'u74': u0**74,                       # U0⁷⁴
        'u76': u0**76,                       # U0⁷⁶
        'u78': u0**78,                       # U0⁷⁸
        'u80': u0**80,                       # U0⁸⁰
        'u82': u0**82,                       # U0⁸²
        'u84': u0**84,                       # U0⁸⁴
        'u86': u0**86,                       # U0⁸⁶
        'u88': u0**88,                       # U0⁸⁸
        'u90': u0**90,                       # U0⁹⁰
        'u92': u0**92,                       # U0⁹²
        'u94': u0**94,                       # U0⁹⁴
        'u96': u0**96,                       # U0⁹⁶
        'u98': u0**98,                       # U0⁹⁸
        'u100': u0**100,                     # U0¹⁰⁰
    }
    
    return constants 