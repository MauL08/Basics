loop = int(input())
for i in range(loop):
    a,b,c = [int(a) for a in input().split()]
    x = a/(b+c)*b
    print(round(x,8),' ',sep='')