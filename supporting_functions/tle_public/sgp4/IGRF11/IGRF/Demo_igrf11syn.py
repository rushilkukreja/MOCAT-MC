import numpy as np
import matplotlib.pyplot as plt
from GetIGRF11_Coefficients import GetIGRF11_Coefficients
from igrf11syn import igrf11syn, gh

# Load or get coefficients
global gh
try:
    # Try to load from a .npz file if it exists
    data = np.load('GHcoefficients.npz')
    gh = data['gh']
except FileNotFoundError:
    gh, _ = GetIGRF11_Coefficients('GHcoefficients.npz')

fyear = 2009.7
alt = 300
z = np.zeros((360, 180))
dip = np.zeros_like(z)

for long in range(-180, 180):
    for lat in range(-89, 91):
        xyzt = igrf11syn(fyear, alt, lat, long)
        z[long + 180, lat + 89] = xyzt[2]
        dip[long + 180, lat + 89] = np.arctan2(xyzt[2], np.sqrt(xyzt[0] ** 2 + xyzt[1] ** 2))

plt.figure()
plt.imshow(z.T, extent=[-180, 179, -89, 90], origin='lower', aspect='auto')
plt.colorbar()
plt.xlabel('Longitude--deg')
plt.ylabel('Latitude--deg')
plt.title('Bz--at alt=0 NTeslas')

zlon_deg = np.arange(-180, 180)
zlat_deg = np.arange(-89, 91)
plt.figure()
plt.imshow(z.T, extent=[-180, 179, -89, 90], origin='lower', aspect='auto')
plt.colorbar()
plt.xlabel('Longitude--deg')
plt.ylabel('Latitude--deg')
plt.title('Bz--at alt=0 NTeslas')

# An equator location of interest
rtd = 180 / np.pi
origin_llh = [-0.0453, -0.7716, 48.2000]
plt.plot(origin_llh[1] * rtd, origin_llh[0] * rtd, 'mp')

# Contour overlay
LINESPEC = 'w'
CS = plt.contour(zlon_deg, zlat_deg, z.T, 20, colors=LINESPEC)
plt.clabel(CS, inline=1, fontsize=10)

# Save data
np.savez('Bz300.npz', zlon_deg=zlon_deg, zlat_deg=zlat_deg, z=z, dip=dip) 