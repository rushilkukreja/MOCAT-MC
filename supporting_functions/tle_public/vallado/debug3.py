def debug3(dbgfile, cosim, emsq, argpo, s1, s2, s3, s4, s5, sinim, ss1, ss2, ss3, ss4, 
           ss5, sz1, sz3, sz11, sz13, sz21, sz23, sz31, sz33, t, tc, gsto, mo, mdot, 
           no, nodeo, nodedot, xpidot, z1, z3, z11, z13, z21, z23, z31, z33, em, 
           argpm, inclm, mm, nm, nodem, irez, atime, d2201, d2211, d3210, d3222, 
           d4410, d4422, d5220, d5232, d5421, d5433, dedt, didt, dmdt, dndt, dnodt, 
           domdt, del1, del2, del3, xfact, xlamo, xli, xni):
    """
    debug3.m - Debug output after dsinit function
    """
    print(f'{"-" * 84}', file=dbgfile)
    print('    inputs :', file=dbgfile)
    print(f'{"cosim":>7}{cosim:15.9f}{"emsq":>7}{emsq:15.9f}{"argpo":>7}{argpo:15.9f}{"s1":>7}{s1:15.9f}{"s2":>7}{s2:15.9f}{"s3":>7}{s3:15.9f}', file=dbgfile)
    print(f'{"s4":>7}{s4:15.9f}{"s5":>7}{s5:15.9f}{"sinim":>7}{sinim:15.9f}{"ss1":>7}{ss1:15.9f}{"ss2":>7}{ss2:15.9f}{"ss3":>7}{ss3:15.9f}', file=dbgfile)
    print(f'{"ss4":>7}{ss4:15.9f}{"ss5":>7}{ss5:15.9f}{"sz1":>7}{sz1:15.9f}{"sz3":>7}{sz3:15.9f}{"sz11":>7}{sz11:15.9f}{"sz13":>7}{sz13:15.9f}', file=dbgfile)
    print(f'{"sz21":>7}{sz21:15.9f}{"sz23":>7}{sz23:15.9f}{"sz31":>7}{sz31:15.9f}{"sz33":>7}{sz33:15.9f}{"t":>7}{t:15.9f}{"tc":>7}{tc:15.9f}', file=dbgfile)
    print(f'{"gsto":>7}{gsto:15.9f}{"mo":>7}{mo:15.9f}{"mdot":>7}{mdot:15.9f}{"no":>7}{no:15.9f}{"nodeo":>7}{nodeo:15.9f}{"nodedot":>7}{nodedot:15.9f}', file=dbgfile)
    print(f'{"xpidot":>7}{xpidot:15.9f}{"z1":>7}{z1:15.9f}{"z3":>7}{z3:15.9f}{"z11":>7}{z11:15.9f}{"z13":>7}{z13:15.9f}{"z21":>7}{z21:15.9f}', file=dbgfile)
    print(f'{"z23":>7}{z23:15.9f}{"z31":>7}{z31:15.9f}{"z33":>7}{z33:15.9f}', file=dbgfile)
    print('    in / out :', file=dbgfile)
    print(f'{"em":>7}{em:15.9f}{"argpm":>7}{argpm:15.9f}{"inclm":>7}{inclm:15.9f}{"mm":>7}{mm:15.9f}{"nm":>7}{nm:15.9f}{"nodem":>7}{nodem:15.9f}', file=dbgfile)
    print('    outputs :', file=dbgfile)
    print(f'{"irez":>7}{irez:15d}{"atime":>7}{atime:15.9f}{"d2201":>7}{d2201:15.9f}{"d2211":>7}{d2211:15.9f}{"d3210":>7}{d3210:15.9f}{"d3222":>7}{d3222:15.9f}', file=dbgfile)
    print(f'{"d4410":>7}{d4410:15.9f}{"d4422":>7}{d4422:15.9f}{"d5220":>7}{d5220:15.9f}{"d5232":>7}{d5232:15.9f}{"d5421":>7}{d5421:15.9f}{"d5433":>7}{d5433:15.9f}', file=dbgfile)
    print(f'{"dedt":>7}{dedt:15.9f}{"didt":>7}{didt:15.9f}{"dmdt":>7}{dmdt:15.9f}{"dndt":>7}{dndt:15.9f}{"dnodt":>7}{dnodt:15.9f}{"domdt":>7}{domdt:15.9f}', file=dbgfile)
    print(f'{"del1":>7}{del1:15.9f}{"del2":>7}{del2:15.9f}{"del3":>7}{del3:15.9f}{"xfact":>7}{xfact:15.9f}{"xlamo":>7}{xlamo:15.9f}{"xli":>7}{xli:15.9f}', file=dbgfile)
    print(f'{"xni":>7}{xni:15.9f}', file=dbgfile) 