import math
loop = int(input())
for i in range(loop):
    x = 0
    y = 0
    n = input()
    for a in n:
        if 'A' in a:
            x = x+1
        if 'B' in a:
            x = x + math.cos(60 * math.pi / 180)
            y = y + math.sin(60 * math.pi / 180)
        if 'C' in a:
            x = x - math.cos(60 * math.pi / 180)
            y = y + math.sin(60 * math.pi / 180)
        if 'D' in a:
            x = x-1
        if 'E' in a:
            x = x - math.cos(60 * math.pi / 180)
            y = y - math.sin(60 * math.pi / 180)
        if 'F' in a:
            x = x + math.cos(60 * math.pi / 180)
            y = y - math.sin(60 * math.pi / 180)
    seq = math.sqrt(x*x + y*y)
    print(round(seq,8),end=' ')
