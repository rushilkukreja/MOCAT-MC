import numpy as np

def seebatt(v):
    """
    Recursion algorithm needed by the lambertbattin routine.
    """
    c = np.zeros(21)
    c[0] = 0.2
    c[1] = 9.0 / 35.0
    c[2] = 16.0 / 63.0
    c[3] = 25.0 / 99.0
    c[4] = 36.0 / 143.0
    c[5] = 49.0 / 195.0
    c[6] = 64.0 / 255.0
    c[7] = 81.0 / 323.0
    c[8] = 100.0 / 399.0
    c[9] = 121.0 / 483.0
    c[10] = 144.0 / 575.0
    c[11] = 169.0 / 675.0
    c[12] = 196.0 / 783.0
    c[13] = 225.0 / 899.0
    c[14] = 256.0 / 1023.0
    c[15] = 289.0 / 1155.0
    c[16] = 324.0 / 1295.0
    c[17] = 361.0 / 1443.0
    c[18] = 400.0 / 1599.0
    c[19] = 441.0 / 1763.0
    c[20] = 484.0 / 1935.0
    sqrtopv = np.sqrt(1.0 + v)
    eta = v / (1.0 + sqrtopv) ** 2
    delold = 1.0
    termold = c[0]
    sum1 = termold
    i = 1
    while i <= 20 and abs(termold) > 1e-6:
        delv = 1.0 / (1.0 + c[i] * eta * delold)
        term = termold * (delv - 1.0)
        sum1 = sum1 + term
        i += 1
        delold = delv
        termold = term
    seebatt_val = 1.0 / ((1.0 / (8.0 * (1.0 + sqrtopv))) * (3.0 + sum1 / (1.0 + eta * sum1)))
    # Second recursion (not used in original return, but included for completeness)
    c2 = np.zeros(20)
    c2[0] = 9.0 / 7.0
    c2[1] = 16.0 / 63.0
    c2[2] = 25.0 / 99.0
    c2[3] = 36.0 / 143.0
    c2[4] = 49.0 / 195.0
    c2[5] = 64.0 / 255.0
    c2[6] = 81.0 / 323.0
    c2[7] = 100.0 / 399.0
    c2[8] = 121.0 / 483.0
    c2[9] = 144.0 / 575.0
    c2[10] = 169.0 / 675.0
    c2[11] = 196.0 / 783.0
    c2[12] = 225.0 / 899.0
    c2[13] = 256.0 / 1023.0
    c2[14] = 289.0 / 1155.0
    c2[15] = 324.0 / 1295.0
    c2[16] = 361.0 / 1443.0
    c2[17] = 400.0 / 1599.0
    c2[18] = 441.0 / 1763.0
    ktr = 20
    sum2 = 0.0
    term2 = 1.0 + c2[ktr - 1] * eta
    for i in range(1, ktr - 1):
        sum2 = c2[ktr - i - 1] * eta / term2
        term2 = 1.0 + sum2
    # The second recursion value is not returned, but could be if needed
    return seebatt_val 