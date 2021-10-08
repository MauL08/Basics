loop = int(input())
for i in range(loop):
    a,b = input().split()
    a = int(a)
    b = int(b)
    x = a/b

    print (round(x),end=' ')