def debug5(dbgfile, satn, yr, ecco, epoch, inclo, no, method, ainv, ao, con41, con42, 
           cosio, cosio2, einv, eccsq, omeosq, posq, rp, rteosq, sinio, gsto):
    """
    debug5.m - Debug output after initl function
    """
    print(f'{"-" * 85}', file=dbgfile)
    print('    inputs :', file=dbgfile)
    print(f'{"satn":>7}{satn:15d}{"yr":>7}{yr:>15}{"ecco":>7}{ecco:15.9f}{"epoch":>7}{epoch:15.9f}{"inclo":>7}{inclo:15.9f}', file=dbgfile)
    print('    in/out :', file=dbgfile)
    print(f'{"no":>7}{no:15.9f}', file=dbgfile)
    print('    outputs :', file=dbgfile)
    print(f'{"method":>7}{method:>15}{"ainv":>7}{ainv:15.9f}{"ao":>7}{ao:15.9f}{"con41":>7}{con41:15.9f}{"con42":>7}{con42:15.9f}{"cosio":>7}{cosio:15.9f}', file=dbgfile)
    print(f'{"cosio2":>7}{cosio2:15.9f}', file=dbgfile)
    print(f'{"einv":>7}{einv:15.9f}{"eccsq":>7}{eccsq:15.9f}{"omeosq":>7}{omeosq:15.9f}{"posq":>7}{posq:15.9f}{"rp":>7}{rp:15.9f}{"rteosq":>7}{rteosq:15.9f}', file=dbgfile)
    print(f'{"sinio":>7}{sinio:15.9f}{"gsto":>7}{gsto:15.9f}', file=dbgfile) 