import numpy as np

def truemean(ttt, order, eqeterms, opt):
    """
    Forms the transformation matrix to go between the norad true equator mean equinox of date and the mean equator mean equinox of date (eci).
    """
    deg2rad = np.pi / 180.0
    # Placeholder for iau80in
    def iau80in():
        return np.zeros((order, 5)), np.zeros((order, 4))
    iar80, rar80 = iau80in()
    ttt2 = ttt * ttt
    ttt3 = ttt2 * ttt
    ttt4 = ttt2 * ttt2
    meaneps = -46.8150 * ttt - 0.00059 * ttt2 + 0.001813 * ttt3 + 84381.448
    meaneps = np.remainder(meaneps / 3600.0, 360.0)
    meaneps = meaneps * deg2rad
    l = 134.96340251 + (1717915923.2178 * ttt + 31.8792 * ttt2 + 0.051635 * ttt3 - 0.00024470 * ttt4) / 3600.0
    l1 = 357.52910918 + (129596581.0481 * ttt - 0.5532 * ttt2 - 0.000136 * ttt3 - 0.00001149 * ttt4) / 3600.0
    f = 93.27209062 + (1739527262.8478 * ttt - 12.7512 * ttt2 + 0.001037 * ttt3 + 0.00000417 * ttt4) / 3600.0
    d = 297.85019547 + (1602961601.2090 * ttt - 6.3706 * ttt2 + 0.006593 * ttt3 - 0.00003169 * ttt4) / 3600.0
    omega = 125.04455501 + (-6962890.2665 * ttt + 7.4722 * ttt2 + 0.007702 * ttt3 - 0.00005939 * ttt4) / 3600.0
    l = np.remainder(l, 360.0) * deg2rad
    l1 = np.remainder(l1, 360.0) * deg2rad
    f = np.remainder(f, 360.0) * deg2rad
    d = np.remainder(d, 360.0) * deg2rad
    omega = np.remainder(omega, 360.0) * deg2rad
    deltapsi = 0.0
    deltaeps = 0.0
    for i in range(order):
        tempval = iar80[i, 0] * l + iar80[i, 1] * l1 + iar80[i, 2] * f + iar80[i, 3] * d + iar80[i, 4] * omega
        deltapsi += (rar80[i, 0] + rar80[i, 1] * ttt) * np.sin(tempval)
        deltaeps += (rar80[i, 2] + rar80[i, 3] * ttt) * np.cos(tempval)
    deltapsi = np.remainder(deltapsi, 360.0) * deg2rad
    deltaeps = np.remainder(deltaeps, 360.0) * deg2rad
    trueeps = meaneps + deltaeps
    cospsi = np.cos(deltapsi)
    sinpsi = np.sin(deltapsi)
    coseps = np.cos(meaneps)
    sineps = np.sin(meaneps)
    costrueeps = np.cos(trueeps)
    sintrueeps = np.sin(trueeps)
    jdttt = ttt * 36525.0 + 2451545.0
    if (jdttt > 2450449.5) and (eqeterms > 0):
        eqe = deltapsi * np.cos(meaneps) + 0.00264 * np.pi / (3600 * 180) * np.sin(omega) + 0.000063 * np.pi / (3600 * 180) * np.sin(2.0 * omega)
    else:
        eqe = deltapsi * np.cos(meaneps)
    nut = np.zeros((3, 3))
    nut[0, 0] = cospsi
    nut[0, 1] = costrueeps * sinpsi if opt != 'b' else 0.0
    nut[0, 2] = sintrueeps * sinpsi
    nut[1, 0] = -coseps * sinpsi if opt != 'b' else 0.0
    nut[1, 1] = costrueeps * coseps * cospsi + sintrueeps * sineps
    nut[1, 2] = sintrueeps * coseps * cospsi - sineps * costrueeps
    nut[2, 0] = -sineps * sinpsi
    nut[2, 1] = costrueeps * sineps * cospsi - sintrueeps * coseps
    nut[2, 2] = sintrueeps * sineps * cospsi + costrueeps * coseps
    st = np.zeros((3, 3))
    st[0, 0] = np.cos(eqe)
    st[0, 1] = -np.sin(eqe)
    st[1, 0] = np.sin(eqe)
    st[1, 1] = np.cos(eqe)
    st[2, 2] = 1.0
    nutteme = nut @ st
    if opt == 'c':
        nutteme = np.eye(3)
        nutteme[0, 2] = deltapsi * sineps
        nutteme[1, 2] = deltaeps
        nutteme[2, 0] = -deltapsi * sineps
        nutteme[2, 1] = -deltaeps
    return deltapsi, trueeps, meaneps, omega, eqe, nutteme 