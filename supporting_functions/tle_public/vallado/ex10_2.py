"""
    -----------------------------------------------------------------
    
                              ex10_2.py
    
  this file demonstrates example 10-2.
    
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

def ex10_2():
    # problem 2
    print('problem 2 -------------------------')
    xo = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    yo = np.array([1, 1, 2, 3, 3, 4, 7, 6])
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

    yc = ans[0] + ans[1] * xo
    print('yc  ', ' '.join(f'{y:11.7f}' for y in yc))
    res = yo - yc
    print('res ', ' '.join(f'{r:11.7f}' for r in res))

    rms = np.sqrt(1/8 * np.sum(res * res))
    conv = np.sqrt(np.sum(res * res) / 7)
    print(f'sum res 2 {np.sum(res * res):11.7f}  rms {rms:11.7f}  sum res /7 {conv:11.7f}')
    print(f'adjusted cov {conv*np.sqrt(atai[0,0]):11.7f}  {conv*np.sqrt(atai[1,1]):11.7f}')

    # problem 2 with bad meas so only 7
    print('problem 2 with bad meas so only 7 -------------------------')
    xo = np.array([1, 2, 3, 4, 5, 6, 8])
    yo = np.array([1, 1, 2, 3, 3, 4, 6])
    print('xo', ' '.join(f'{x:3d}' for x in xo))
    print('yo', ' '.join(f'{y:3d}' for y in yo))

    ata = np.array([[7, np.sum(xo)], [np.sum(xo), np.sum(xo * xo)]])
    atb = np.array([np.sum(yo), np.sum(xo * yo)])
    atai = np.linalg.inv(ata)
    ans = atai @ atb
    print('ata =\n', ata)
    print('atb =\n', atb)
    print('atai =\n', atai)
    print('ans =\n', ans)

    yc = ans[0] + ans[1] * xo
    res = yo - yc
    rms = np.sqrt(1/7 * np.sum(res * res))
    conv = np.sqrt(np.sum(res * res) / 6)
    print(f'sum res 2 {np.sum(res * res):11.7f}  rms {rms:11.7f}  sum res /7 {conv:11.7f}')
    print(f'adjusted cov {conv*np.sqrt(atai[0,0]):11.7f}  {conv*np.sqrt(atai[1,1]):11.7f}')

    # problem 3 example with weighting
    print('problem 3 with weight added in, original 8 obs -------------------------')
    xo = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    yo = np.array([1, 1, 2, 3, 3, 4, 4, 6])
    print('xo', ' '.join(f'{x:3d}' for x in xo))
    print('yo', ' '.join(f'{y:3d}' for y in yo))

    w1 = 1.0 / 0.1
    w2 = 1.0 / 0.02
    w = np.zeros((8, 8))
    w[0, 0] = w1
    w[1, 1] = w2
    w[2, 2] = w1
    w[3, 3] = w2
    w[4, 4] = w1
    w[5, 5] = w2
    w[6, 6] = w1
    w[7, 7] = w2

    i = np.ones((8, 1))
    a = np.hstack((i, xo.reshape(-1, 1)))
    b = yo.reshape(-1, 1)
    atw = a.T @ w
    atwa = a.T @ w @ a
    atwb = a.T @ w @ b
    atwai = np.linalg.inv(atwa)
    ans = atwai @ atwb
    print('atw =\n', atw)
    print('atwa =\n', atwa)
    print('atwb =\n', atwb)
    print('atwai =\n', atwai)
    print('ans =\n', ans.flatten())

    yc = ans[0] + ans[1] * xo.reshape(-1, 1)
    print('yc  ', ' '.join(f'{y[0]:11.7f}' for y in yc))
    res = yo.reshape(-1, 1) - yc
    print('res ', ' '.join(f'{r[0]:11.7f}' for r in res))

    rms = np.sqrt(1/8 * np.sum(res ** 2))
    conv = np.sqrt(np.sum(res ** 2) / 7)
    print(f'sum res 2 {np.sum(res ** 2):11.7f}  rms {rms:11.7f}  sum res /7 {conv:11.7f}')
    print(f'adjusted cov {conv*np.sqrt(atai[0,0]):11.7f}  {conv*np.sqrt(atai[1,1]):11.7f}')

if __name__ == "__main__":
    ex10_2() 