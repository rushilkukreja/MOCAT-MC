def debug2(dbgfile, epoch, ep, argpp, tc, inclp, nodep, np, snodm, cnodm, sinim, cosim, 
           sinomm, cosomm, day, e3, ee2, em, emsq, gam, peo, pgho, pho, pinco, plo, 
           rtemsq, se2, se3, sgh2, sgh3, sgh4, sh2, sh3, si2, si3, sl2, sl3, sl4, s1, s2, 
           s3, s4, s5, s6, s7, ss1, ss2, ss3, ss4, ss5, ss6, ss7, sz1, sz2, sz3, sz11, 
           sz12, sz13, sz21, sz22, sz23, sz31, sz32, sz33, xgh2, xgh3, xgh4, xh2, xh3, 
           xi2, xi3, xl2, xl3, xl4, nm, z1, z2, z3, z11, z12, z13, z21, z22, z23, z31, 
           z32, z33, zmol, zmos):
    """
    debug2.m - Debug output after dscom function
    """
    print(f'{"-" * 84}', file=dbgfile)
    print('    inputs :', file=dbgfile)
    print(f'{"epoch":>7}{epoch:15.9f}{"ep":>7}{ep:15.9f}{"argpp":>7}{argpp:15.9f}{"tc":>7}{tc:15.9f}{"inclp":>7}{inclp:15.9f}{"nodep":>7}{nodep:15.9f}', file=dbgfile)
    print(f'{"np":>7}{np:15.9f}', file=dbgfile)
    print('    outputs :', file=dbgfile)
    print(f'{"snodm":>7}{snodm:15.9f}{"cnodm":>7}{cnodm:15.9f}{"sinim":>7}{sinim:15.9f}{"cosim":>7}{cosim:15.9f}{"sinomm":>7}{sinomm:15.9f}{"cosomm":>7}{cosomm:15.9f}', file=dbgfile)
    print(f'{"day":>7}{day:15.9f}{"e3":>7}{e3:15.9f}{"ee2":>7}{ee2:15.9f}{"em":>7}{em:15.9f}{"emsq":>7}{emsq:15.9f}{"gam":>7}{gam:15.9f}', file=dbgfile)
    print(f'{"peo":>7}{peo:15.9f}{"pgho":>7}{pgho:15.9f}{"pho":>7}{pho:15.9f}{"pinco":>7}{pinco:15.9f}{"plo":>7}{plo:15.9f}', file=dbgfile)
    print(f'{"rtemsq":>7}{rtemsq:15.9f}{"se2":>7}{se2:15.9f}{"se3":>7}{se3:15.9f}{"sgh2":>7}{sgh2:15.9f}{"sgh3":>7}{sgh3:15.9f}{"sgh4":>7}{sgh4:15.9f}', file=dbgfile)
    print(f'{"sh2":>7}{sh2:15.9f}{"sh3":>7}{sh3:15.9f}{"si2":>7}{si2:15.9f}{"si3":>7}{si3:15.9f}{"sl2":>7}{sl2:15.9f}{"sl3":>7}{sl3:15.9f}', file=dbgfile)
    print(f'{"sl4":>7}{sl4:15.9f}{"s1":>7}{s1:15.9f}{"s2":>7}{s2:15.9f}{"s3":>7}{s3:15.9f}{"s4":>7}{s4:15.9f}{"s5":>7}{s5:15.9f}', file=dbgfile)
    print(f'{"s6":>7}{s6:15.9f}{"s7":>7}{s7:15.9f}{"ss1":>7}{ss1:15.9f}{"ss2":>7}{ss2:15.9f}{"ss3":>7}{ss3:15.9f}{"ss4":>7}{ss4:15.9f}', file=dbgfile)
    print(f'{"ss5":>7}{ss5:15.9f}{"ss6":>7}{ss6:15.9f}{"ss7":>7}{ss7:15.9f}{"sz1":>7}{sz1:15.9f}{"sz2":>7}{sz2:15.9f}{"sz3":>7}{sz3:15.9f}', file=dbgfile)
    print(f'{"sz11":>7}{sz11:15.9f}{"sz12":>7}{sz12:15.9f}{"sz13":>7}{sz13:15.9f}{"sz21":>7}{sz21:15.9f}{"sz22":>7}{sz22:15.9f}{"sz23":>7}{sz23:15.9f}', file=dbgfile)
    print(f'{"sz31":>7}{sz31:15.9f}{"sz32":>7}{sz32:15.9f}{"sz33":>7}{sz33:15.9f}{"xgh2":>7}{xgh2:15.9f}{"xgh3":>7}{xgh3:15.9f}{"xgh4":>7}{xgh4:15.9f}', file=dbgfile)
    print(f'{"xh2":>7}{xh2:15.9f}{"xh3":>7}{xh3:15.9f}{"xi2":>7}{xi2:15.9f}{"xi3":>7}{xi3:15.9f}{"xl2":>7}{xl2:15.9f}{"xl3":>7}{xl3:15.9f}', file=dbgfile)
    print(f'{"xl4":>7}{xl4:15.9f}{"nm":>7}{nm:15.9f}{"z1":>7}{z1:15.9f}{"z2":>7}{z2:15.9f}{"z3":>7}{z3:15.9f}{"z11":>7}{z11:15.9f}', file=dbgfile)
    print(f'{"z12":>7}{z12:15.9f}{"z13":>7}{z13:15.9f}{"z21":>7}{z21:15.9f}{"z22":>7}{z22:15.9f}{"z23":>7}{z23:15.9f}{"z31":>7}{z31:15.9f}', file=dbgfile)
    print(f'{"z32":>7}{z32:15.9f}{"z33":>7}{z33:15.9f}{"zmol":>7}{zmol:15.9f}{"zmos":>7}{zmos:15.9f}', file=dbgfile) 