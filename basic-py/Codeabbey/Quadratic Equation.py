import math
loop = int(input())
for i in range(loop):
    a,b,c = [int(x) for x in input().split()]

    d = b * b - 4 * a *c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        x1 = int(x1)
        x2 = int(x2)
        print(x1,' ',x2,'; ',sep='')
    elif d == 0:
        x1 = -b / (2 * a)
        x2 = -b / (2 * a)
        x1 = int(x1)
        x2 = int(x2)
        print(x1,' ',x2,'; ',sep='')
    else:
        r = -b / (2 * a)
        i = math.sqrt(-d) / (2 * a)
        r = int(r)
        i = int(i)
        print(r,'+',i,'i',' ',r,'-',i,'i','; ',sep='')