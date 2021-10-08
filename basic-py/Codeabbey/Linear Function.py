loop = int(input())
for i in range(loop):
    x1,y1,x2,y2 = [int(x1) for x1 in input().split()]

    m = (y2-y1)/(x2-x1)
    c = y1-(m*x1)

    print('(',int(m),' ',int(c),')',' ',sep='')