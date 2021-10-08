def GCD(x,y):
    while(x != y):
        if y > x:
            y -= x
        else:
            x -= y
    return y

loop = int(input())
for i in range(loop):
    a,b = input().split()
    a = int(a)
    b = int(b)

    LCM = a*b/GCD(a,b)

    print('(',GCD(a,b),' ',int(LCM),')',' ',sep='')