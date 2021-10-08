loop = int(input())
for i in range(loop):
    inc = 0

    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    x = (a*b) + c
    x = int(x)

    while x != 0:
        inc = inc + int(x % 10)
        x = int(x / 10)

    print(inc,' ',sep='')

