loop = int(input())
for i in range(loop):
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a > b:
        c = b
    if a < b:
        c = a
    print(c,end=' ')