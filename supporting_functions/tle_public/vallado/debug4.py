def debug4(dbgfile, irez, d2201, d2211, d3210, d3222, d4410, d4422, d5220, d5232, d5421, 
           d5433, dedt, del1, del2, del3, didt, dmdt, dnodt, domdt, argpo, argpdot, t, 
           tc, gsto, xfact, xlamo, no, atime, em, argpm, inclm, xli, mm, xni, dndt, nm):
    """
    debug4.m - Debug output after dspace function
    """
    print(f'{"-" * 84}', file=dbgfile)
    print('    inputs :', file=dbgfile)
    print(f'{"irez":>7}{irez:15d}{"d2201":>7}{d2201:15.9f}{"d2211":>7}{d2211:15.9f}{"d3210":>7}{d3210:15.9f}{"d3222":>7}{d3222:15.9f}{"d4410":>7}{d4410:15.9f}', file=dbgfile)
    print(f'{"d4422":>7}{d4422:15.9f}{"d5220":>7}{d5220:15.9f}{"d5232":>7}{d5232:15.9f}{"d5421":>7}{d5421:15.9f}{"d5433":>7}{d5433:15.9f}{"dedt":>7}{dedt:15.9f}', file=dbgfile)
    print(f'{"del1":>7}{del1:15.9f}{"del2":>7}{del2:15.9f}{"del3":>7}{del3:15.9f}{"didt":>7}{didt:15.9f}{"dmdt":>7}{dmdt:15.9f}{"dnodt":>7}{dnodt:15.9f}', file=dbgfile)
    print(f'{"domdt":>7}{domdt:15.9f}{"argpo":>7}{argpo:15.9f}{"argpdot":>7}{argpdot:15.9f}{"t":>7}{t:15.9f}{"tc":>7}{tc:15.9f}{"gsto":>7}{gsto:15.9f}', file=dbgfile)
    print(f'{"xfact":>7}{xfact:15.9f}{"xlamo":>7}{xlamo:15.9f}{"no":>7}{no:15.9f}', file=dbgfile)
    print('    in / out :', file=dbgfile)
    print(f'{"atime":>7}{atime:15.9f}{"em":>7}{em:15.9f}{"argpm":>7}{argpm:15.9f}{"inclm":>7}{inclm:15.9f}{"xli":>7}{xli:15.9f}{"mm":>7}{mm:15.9f}', file=dbgfile)
    print(f'{"xni":>7}{xni:15.9f}{"nodem":>7}{nodem:15.9f}', file=dbgfile)
    print('    outputs :', file=dbgfile)
    print(f'{"dndt":>7}{dndt:15.9f}{"nm":>7}{nm:15.9f}', file=dbgfile) 