import math
def binary(A,B,C,D,x):
    seq = (A*x)+(B*math.sqrt(x*x*x))-(C*math.exp(-x/50))-D
    return seq

loop = int(input())
for i in range(loop):
    a,b,c,d = [float(p) for p in input().split()]
    x = 0
    x1 = 0
    x2 = 100

    while x2-x1 > math.pow(10,-7):
        if binary(a,b,c,d,x) < 0:
            x1 = x
        elif binary(a,b,c,d,x) >= 0:
            x2 = x

        x = (x1+x2)/2

    print(x,end=' ')
