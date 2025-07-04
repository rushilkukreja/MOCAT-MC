import numpy as np

def findIpeaks(datas, thresh, iSubset, *args):
    """
    Find 2D peak clusters above threshold with size truncation.
    
    Parameters:
    -----------
    datas : array-like
        ny x nx data array
    thresh : array-like
        Threshold in data units
    iSubset : array-like
        Indices of points included, [] for full set
    *args : tuple
        Optional arguments:
        - minHits: minimum # of hits for cluster (default: 2)
        - dXmax: max extent of cluster x coordinates (default: 5)
        - dYmax: max extent of cluster y coordinates (default: 5)
    
    Returns:
    --------
    peaks : list
        List of peak dictionaries with keys:
        - pos: index location in datas of brightest peak [ix, iy]
        - Ibar: value of brightest peak
        - Hits: # of peaks in cluster
    """
    if len(args) == 0:
        # Parameters for peak extraction
        dXmax = 5
        dYmax = 5  # Maximum size
        # NOTE: Too small => multiple hits on same peak
        #       Too large => joins adjacent peaks
        minHits = 2  # Minimum # of hits in peak
    else:
        minHits = args[0]
        dXmax = args[1]
        dYmax = args[2]
    
    n1, n2 = datas.shape
    data = np.zeros((n1, n2))
    data.flat[iSubset] = datas.flat[iSubset]
    
    # Find peaks above threshold
    iPeaks = np.where(data > thresh)[0]
    Peaks = data.flat[iPeaks]
    npeaks = len(iPeaks)
    
    # Order the Peaks and find their coordinate indices
    sort_idx = np.argsort(Peaks)[::-1]  # descending order
    Peaks = Peaks[sort_idx]
    iPeaks = iPeaks[sort_idx]
    iy, ix = np.unravel_index(iPeaks, (n1, n2))
    
    peaks = []
    nPeaks2test = npeaks
    iCount = 0
    
    while nPeaks2test > minHits:
        # Find the neighbors of the current brightest peak (include the test peak in the set)
        ixtest = ix[0]
        iytest = iy[0]
        
        # Test X and Y distances separately
        dX = np.abs(ix - ixtest)
        iHitsX = np.where(dX < dXmax)[0]
        dY = np.abs(iy - iytest)
        iHitsY = np.where(dY < dYmax)[0]
        iHitsP = np.intersect1d(iHitsX, iHitsY)  # Locations in Peaks
        iHits = (ix[iHitsP] - 1) * n1 + iy[iHitsP]  # Locations in data
        
        # Save the current peak if it has enough neighbors
        if len(iHits) > minHits:
            iCount += 1
            peakVals = np.ones((2, 1)) * Peaks[iHitsP].reshape(1, -1)  # peak Values
            peaks.append({
                'pos': [iytest, ixtest],  # Brightest peak in current cluster
                'Ibar': data[iytest, ixtest],
                'Hits': len(peakVals[0])
            })
        
        # Remove the current brightest peak and its neighbors
        iPeaks = np.setdiff1d(iPeaks, iHits)
        Peaks = data.flat[iPeaks]
        
        # Reorder the remaining peaks
        sort_idx = np.argsort(Peaks)[::-1]  # descending order
        Peaks = Peaks[sort_idx]
        iPeaks = iPeaks[sort_idx]
        iy, ix = np.unravel_index(iPeaks, (n1, n2))
        nPeaks2test = len(iPeaks)
    
    return peaks 