import numpy as np
import matplotlib.pyplot as plt

# Test tcs2height
# USEFUL CONVERSIONS
# 1 m  =  .3048 ft
# 1 mi (statute)  = 1.607 km
# 1 mi (nautical) = 1.852 km 
rtd = 180 / np.pi
dtr = np.pi / 180
Re = 6378166
ft2m = 0.3048

# Dam Neck Radar
Rlat = 36.7788  # 36 46.73'  N
Rlon = -75.9573  # 75 57.44'  W
Rheight = 22  # Approx height of antenna (phase center?)
origin = np.array([Rlat, Rlon, 0]) * dtr

# Generate a tcs file
nsamp = 2000
x = np.linspace(0, 300000, nsamp)
y = x
z = -100 * np.ones_like(x)
rng = np.sqrt(x**2 + y**2 + z**2)
tcs = np.vstack([x, y, z])

# Generate height from surface to tcs (negative => below surface)
# Note: tcs2heightT function needs to be imported from GPS_CoordinateXforms
# height = tcs2heightT(tcs, origin)      # Call with origin => WGS84 ellipsoid
# height0 = tcs2heightT(tcs)             # Call with no second argument or empty => Spherical Earth

# Placeholder values for demonstration
height = np.zeros_like(x)
height0 = np.zeros_like(x)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(rng/1000, height/1000, 'r', label='WGS84')
plt.plot(rng/1000, height0/1000, 'm', label='Sphere')
plt.grid(True)
plt.ylabel('height--km')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(rng/1000, height - height0, 'r')
plt.grid(True)
plt.ylabel('diff--m')
plt.xlabel('range--km')
plt.show() 