def GCD(x,y):
    while(x != y):
        if y > x:
            y -= x
        else:
            x -= y
    return y

loop = int(input())
for i in range(loop):
    Sprev = 1
    Scur  = 0
    Tprev = 0
    Tcur  = 1
    a,b = [int(p) for p in input().split()]
    x = a
    y = b
    FPB = GCD(a,b)

    divide = (a / b)
    divide = int(divide)
    modulo = (a % b)
    modulo = int(modulo)

    Snext = Sprev - (divide * Scur)
    Snext = int(Snext)
    Tnext = Tprev - (divide * Tcur)
    Tnext = int(Tnext)

    a = b
    b = modulo

    while modulo != 0:
        divide = (a / b)
        divide = int(divide)
        modulo = (a % b)
        modulo = int(modulo)

        a = b
        b = modulo

        Sprev = Scur
        Scur = Snext

        Tprev = Tcur
        Tcur = Tnext

        Snext = Sprev - (divide * Scur)
        Tnext = Tprev - (divide * Tcur)

    print(int(FPB),int(Scur),int(Tcur),sep=' ',end =' ')

