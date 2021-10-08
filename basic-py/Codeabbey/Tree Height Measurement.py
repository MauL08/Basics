import math

loop = int(input())
for i in range(loop):
    d,sudut = input().split()
    d = int(d)
    sudut = float(sudut)

    rad = math.pi/180

    trigono = math.tan((sudut-90)*rad)

    h = trigono*d

    print(round(h),' ',sep='')
