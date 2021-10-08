loop = int(input())
for i in range(loop):
    a,b,c = [int(a) for a in input().split()]

    if a+b>c and a+c>b and b+c>a:
        x = 1
    else:
        x = 0
    print(x,' ',sep='')