"""
    -----------------------------------------------------------------
    
                              ex10_3.py
    
  this file demonstrates example 10-3.
    
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

def ex10_3():
    # problem 3
    print('problem 3 -------------------------')
    xo = np.array([1, 2, 3, 4])
    yo = np.array([2.5, 8.0, 19.0, 50.0])
    print('xo', ' '.join(f'{x:8d}' for x in xo))
    print('yo', ' '.join(f'{y:8.6f}' for y in yo))

    beta = np.log(yo[3]/yo[2]) / np.log(4/3)
    alpha = yo[2] / 3**beta
    print(f'beta = {beta}')
    print(f'alpha = {alpha}')

    # do first time manually to get intermediate values
    yn = np.zeros(4)
    parynalp = np.zeros(4)
    parynbet = np.zeros(4)
    for i in range(4):
        yn[i] = alpha * xo[i]**beta
        parynalp[i] = xo[i]**beta
        parynbet[i] = alpha * np.log(xo[i]) * xo[i]**beta
    print('yn =', yn)
    print('parynalp =', parynalp)
    print('parynbet =', parynbet)

    ata = np.array([[np.dot(parynalp, parynalp), np.dot(parynalp, parynbet)],
                    [np.dot(parynalp, parynbet), np.dot(parynbet, parynbet)]])
    atb = np.array([np.dot(parynalp, yo-yn), np.dot(parynbet, yo-yn)])
    atai = np.linalg.inv(ata)
    ans = atai @ atb
    print('ata =\n', ata)
    print('atb =\n', atb)
    print('atai =\n', atai)
    print('ans =\n', ans)

    alpha = alpha + ans[0]
    beta = beta + ans[1]

    b = np.zeros(4)
    for j in range(4):
        b[j] = yo[j] - alpha * (xo[j]**beta)
    print('b =', b)
    rms = np.sqrt(np.dot(b, b) / 4)
    rmsold = rms
    print(f'0 dx {ans[0]:11.7f}  {ans[1]:11.7f} ans {alpha:11.7f}  {beta:11.7f} rms {rms:11.7f}')

    for loop in range(1, 4):
        for i in range(4):
            yn[i] = alpha * xo[i]**beta
            parynalp[i] = xo[i]**beta
            parynbet[i] = alpha * np.log(xo[i]) * xo[i]**beta
        ata = np.array([[np.dot(parynalp, parynalp), np.dot(parynalp, parynbet)],
                        [np.dot(parynalp, parynbet), np.dot(parynbet, parynbet)]])
        atb = np.array([np.dot(parynalp, yo-yn), np.dot(parynbet, yo-yn)])
        atai = np.linalg.inv(ata)
        ans = atai @ atb
        alpha = alpha + ans[0]
        beta = beta + ans[1]
        for j in range(4):
            b[j] = yo[j] - alpha * (xo[j]**beta)
        print('b =', b)
        rms = np.sqrt(np.dot(b, b) / 4)
        rmsdel = (rmsold - rms) / rmsold
        print(f'{loop:2d} dx {ans[0]:11.7f}  {ans[1]:11.7f} ans {alpha:11.7f}  {beta:11.7f} rms {rms:11.7f} {rmsdel:11.7f}')
        rmsold = rms

if __name__ == "__main__":
    ex10_3() 