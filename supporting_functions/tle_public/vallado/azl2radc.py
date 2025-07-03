# azl2radc
#
# this function finds the rtasc decl values given the az-el
#
#
#
import numpy as np

def azl2radc(az, el, lat, lst):
    """
    Find the rtasc decl values given the az-el.
    
    Args:
        az: azimuth (rad)
        el: elevation (rad)
        lat: latitude (rad)
        lst: local sidereal time (rad)
        
    Returns:
        rtasc: right ascension (rad)
        decl: declination (rad)
    """
    rad = 180.0 / np.pi
    
    decl = np.arcsin(np.sin(el) * np.sin(lat) + np.cos(el) * np.cos(lat) * np.cos(az))
    
    slha1 = -(np.sin(az) * np.cos(el) * np.cos(lat)) / (np.cos(decl) * np.cos(lat))
    clha1 = (np.sin(el) - np.sin(lat) * np.sin(decl)) / (np.cos(decl) * np.cos(lat))
    
    lha1 = np.arctan2(slha1, clha1)
    print(f" lha1 {lha1*rad:13.7f}")
    
    slha2 = -(np.sin(az) * np.cos(el)) / (np.cos(decl))
    clha2 = (np.cos(lat) * np.sin(el) - np.sin(lat) * np.cos(el) * np.cos(az)) / (np.cos(decl))
    
    lha2 = np.arctan2(slha2, clha2)
    print(f" lha2 {lha2*rad:13.7f}")
    
    rtasc = lst - lha1
    
    return rtasc, decl 