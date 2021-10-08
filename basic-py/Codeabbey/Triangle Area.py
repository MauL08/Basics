loop = int(input())
for i in range(loop):
    x1,y1,x2,y2,x3,y3 = [int(x1) for x1 in input().split()]

    formula = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2

    print(round(formula,1),' ',sep='')