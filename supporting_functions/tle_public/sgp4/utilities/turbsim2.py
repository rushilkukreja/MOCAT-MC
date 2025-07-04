import numpy as np

def turbsim2(rootSDF):
    """
    Generate realization of field with SDF rootSDF.^2.
    
    Parameters:
    -----------
    rootSDF : array-like
        Square root of spectral density function
    
    Returns:
    --------
    simturb : array-like
        Simulated turbulent field
    """
    n1, n2 = rootSDF.shape
    xi = np.zeros((n1, n2), dtype=complex)
    
    # Generate complex random numbers for the first quadrant
    xi[:n1//2+1, :n2//2+1] = (np.random.randn(n1//2+1, n2//2+1) + 
                              1j * np.random.randn(n1//2+1, n2//2+1)) / np.sqrt(2)
    
    # Generate complex random numbers for the second quadrant
    xi[n1//2+1:, 1:n2//2] = (np.random.randn(n1//2-1, n2//2-1) + 
                             1j * np.random.randn(n1//2-1, n2//2-1)) / np.sqrt(2)
    
    # Set DC component to zero
    xi[0, 0] = 0
    
    # Make real for Nyquist frequencies
    xi[0, n2//2] = np.real(xi[0, n2//2]) / 2
    xi[n1//2, 0] = np.real(xi[n1//2, 0]) / 2
    xi[n1//2, n2//2] = np.real(xi[n1//2, n2//2]) / 2
    
    # Apply conjugate symmetry
    xi[n1//2+1:, 0] = np.conj(xi[n1//2-1:0:-1, 0])
    xi[n1//2+1:, n2//2] = np.conj(xi[n1//2-1:0:-1, n2//2])
    xi[0, n2//2+1:] = np.conj(xi[0, n2//2-1:0:-1])
    xi[n1//2, n2//2+1:] = np.conj(xi[n1//2, n2//2-1:0:-1])
    
    xi[1:n1//2, n2//2+1:] = np.conj(xi[n1-1:n1//2:-1, n2//2-1:0:-1])
    xi[n1//2+1:, n2//2+1:] = np.conj(xi[n1//2-1:0:-1, n2//2-1:0:-1])
    
    # NOTE: This scaling preserves variance
    simturb = np.real(np.fft.ifft2(np.fft.ifftshift(rootSDF * xi)))
    
    return simturb 