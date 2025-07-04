import numpy as np
import matplotlib.pyplot as plt

# Demo coordinate manipulations
# Map radar coordinates to surface using precomputed maps
dtr = np.pi / 180

# Radar Location
Rlat = 36.0              
Rlon = -75.0            
Rheight = 30              
RADAR = {
    'Rlat': Rlat * dtr,
    'Rlon': Rlon * dtr,
    'Rheight': Rheight
}

nptsx = 500
nptsy = 200

# Lat-lon boundaries of region to be mapped
lat_min = 35.9
lat_max = 36.1
lon_min = -74.9
lon_max = -75.1

# Define rectangular lat-long grid & mesh
latitude = np.linspace(lat_min, lat_max, nptsx) * dtr
longitude = np.linspace(lon_min, lon_max, nptsy) * dtr

# Note: SurfaceTCSmap function needs to be imported
# R, PHI, x, y, Surf = SurfaceTCSmap(latitude, longitude, RADAR)

# Placeholder values for demonstration
R = np.random.rand(nptsy, nptsx) * 100000  # Range in meters
PHI = np.random.rand(nptsy, nptsx) * 2 * np.pi  # Bearing in radians
x = np.linspace(-50000, 50000, nptsx)  # x coordinates in meters
y = np.linspace(-20000, 20000, nptsy)  # y coordinates in meters

plt.figure()
plt.imshow(R/1000, extent=[x[0]/1000, x[-1]/1000, y[0]/1000, y[-1]/1000], 
           origin='lower', aspect='auto')
plt.colorbar()
plt.title('Range(km) to surface at x-y')
plt.xlabel('x--km')
plt.ylabel('y--km')

plt.figure()
plt.imshow(PHI/dtr, extent=[x[0]/1000, x[-1]/1000, y[0]/1000, y[-1]/1000], 
           origin='lower', aspect='auto')
plt.colorbar()
plt.title('Bearing(deg) to surface at x-y')
plt.xlabel('x--km')
plt.ylabel('y--km')
plt.show() 