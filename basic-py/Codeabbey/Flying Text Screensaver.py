# Set Variables
x = 0
y = 0
x1 = 1
y1 = 1
# Input Value
a,b,c = [int(q) for q in input().split()]
# Set Algorithm
for i in range(101):
    print(x,y,sep=' ',end=' ')

    if y+y1 == b or y+y1 < 0:
        y1 = y1*(-1)

    y = y+y1

    if x+x1+c > a or x+x1 < 0:
        x1 = x1*(-1)

    x = x+x1
