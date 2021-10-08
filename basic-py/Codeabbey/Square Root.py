loop = int(input())
for i in range(loop):
    r = 1
    a,b = [int(x) for x in input().split()]
    for j in range(b):
        r = (r+(a/r))/2
    print(round(r,8),' ',sep='')