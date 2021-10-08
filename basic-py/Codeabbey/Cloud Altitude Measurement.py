import math
loop = int(input())
for i in range(loop):
    a,b,c = [float(x) for x in input().split()]

    rad = math.pi/180

    A = math.tan(b*rad)
    B = math.tan(c*rad)

    h = (A*a)/(1-(A/B))

    print(round(h),' ',sep='')