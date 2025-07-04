import numpy as np
import matplotlib.pyplot as plt

# DisplayRadarHorizon
dtr = np.pi / 180

# Dam Neck Radar
Rlat = 36.7788  # 36 46.73'  N
Rlon = -75.9573  # 75 57.44'  W                       
Rheight = 10000

source0_llh = np.array([Rlat, Rlon, 0]) * dtr + np.array([0, 0, Rheight])

bscan = np.linspace(0, 2*np.pi, 500)
# Note: GHorizon function needs to be imported from GPS_CoordinateXforms
# rangeH, sthetaH, cthetaH = GHorizon(bscan, source0_llh, 0)

# Placeholder values for demonstration
rangeH = np.ones_like(bscan) * 100000
sthetaH = np.ones_like(bscan) * 0.1
cthetaH = np.ones_like(bscan) * 0.99

v_tcs = np.vstack([
    sthetaH * np.cos(bscan),
    sthetaH * np.sin(bscan),
    cthetaH
])

plt.figure()
plt.plot(rangeH * v_tcs[0, :] / 1000, rangeH * v_tcs[1, :] / 1000, 'b')
plt.grid(True)
plt.plot(0, 0, 'mp')
plt.xlabel('X-km')
plt.ylabel('y-km')
plt.title(f'Range to radar horizon from {Rheight}-m height')
plt.show() 