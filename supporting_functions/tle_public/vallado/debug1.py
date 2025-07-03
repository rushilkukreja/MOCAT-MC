def debug1(dbgfile, e3, ee2, peo, pgho, pho, pinco, plo, se2, se3, sgh2, sgh3, sgh4, 
           sh2, sh3, si2, si3, sl2, sl3, sl4, t, xgh2, xgh3, xgh4, xh2, xh3, xi2, xi3, 
           xl2, xl3, xl4, zmol, zmos, init, ep, inclp, nodep, argpp, mp):
    """
    debug1.m - Debug output after dpper function
    """
    print(f'{"-" * 84}', file=dbgfile)
    print('    inputs :', file=dbgfile)
    print(f'{"e3":>7}{e3:15.9f}{"ee2":>7}{ee2:15.9f}{"peo":>7}{peo:15.9f}{"pgho":>7}{pgho:15.9f}{"pho":>7}{pho:15.9f}{"pinco":>7}{pinco:15.9f}', file=dbgfile)
    print(f'{"plo":>7}{plo:15.9f}{"se2":>7}{se2:15.9f}{"se3":>7}{se3:15.9f}{"sgh2":>7}{sgh2:15.9f}{"sgh3":>7}{sgh3:15.9f}{"sgh4":>7}{sgh4:15.9f}', file=dbgfile)
    print(f'{"sh2":>7}{sh2:15.9f}{"sh3":>7}{sh3:15.9f}{"si2":>7}{si2:15.9f}{"si3":>7}{si3:15.9f}{"sl2":>7}{sl2:15.9f}{"sl3":>7}{sl3:15.9f}', file=dbgfile)
    print(f'{"sl4":>7}{sl4:15.9f}{"t":>7}{t:15.9f}{"xgh2":>7}{xgh2:15.9f}{"xgh3":>7}{xgh3:15.9f}{"xgh4":>7}{xgh4:15.9f}{"xh2":>7}{xh2:15.9f}', file=dbgfile)
    print(f'{"xh3":>7}{xh3:15.9f}{"xi2":>7}{xi2:15.9f}{"xi3":>7}{xi3:15.9f}{"xl2":>7}{xl2:15.9f}{"xl3":>7}{xl3:15.9f}{"xl4":>7}{xl4:15.9f}', file=dbgfile)
    print(f'{"zmol":>7}{zmol:15.9f}{"zmos":>7}{zmos:15.9f}{"init":>7}{init:>15}', file=dbgfile)
    print('    in/out :', file=dbgfile)
    print(f'{"ep":>7}{ep:15.9f}{"inclp":>7}{inclp:15.9f}{"nodep":>7}{nodep:15.9f}{"argpp":>7}{argpp:15.9f}{"mp":>7}{mp:15.9f}', file=dbgfile) 