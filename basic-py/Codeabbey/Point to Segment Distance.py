import math
loop = int(input())
for i in range(loop):
    x1,y1,x2,y2,xp,yp = [int(x) for x in input().split()]
    t = -1*(((x1-xp)*(x2-x1))+((y1-yp)*(y2-y1)))/((math.pow((x2-x1),2))+(math.pow((y2-y1),2)))
    if t >= 0 and t <= 1:
        d = abs((x2 - x1) * (y1 - yp) - (y2 - y1) * (x1 - xp)) / (math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)))
        status = d
    else:
        d1 = math.sqrt(math.pow((x2 - xp), 2) + math.pow((y2 - yp), 2))
        d2 = math.sqrt(math.pow((x1 - xp), 2) + math.pow((y1 - yp), 2))
        if d1 < d2:
            status = d1
        elif d1 > d2:
            status = d2
    print(round(status,8),end=' ')