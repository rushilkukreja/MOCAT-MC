"""
    -----------------------------------------------------------------
    
                              ex10_1.py
    
  this file demonstrates example 10-1.
    
                          companion code for
             fundamentals of astrodyanmics and applications
                                 2007
                            by david vallado
    
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
             7 jun 07  david vallado
                         original
  changes :
            13 feb 07  david vallado
                         original baseline
    
     *****************************************************************
"""

import numpy as np

def ex10_1():
    # problem 1
    print('problem 1 --------------------------')
    xo = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    yo = np.array([1, 1, 2, 3, 3, 4, 4, 6])
    print('xo', ' '.join(f'{x:3d}' for x in xo))
    print('yo', ' '.join(f'{y:3d}' for y in yo))

    ata = np.array([[8, np.sum(xo)], [np.sum(xo), np.sum(xo * xo)]])
    atb = np.array([np.sum(yo), np.sum(xo * yo)])
    atai = np.linalg.inv(ata)
    ans = atai @ atb
    print('ata =\n', ata)
    print('atb =\n', atb)
    print('atai =\n', atai)
    print('ans =\n', ans)

if __name__ == "__main__":
    ex10_1() 