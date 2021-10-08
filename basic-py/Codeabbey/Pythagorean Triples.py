loop = int(input())
for i in range(loop):
    n = 0
    x = 0
    y = int(input())
    while n != y:
        for j in range(1,x):
            a = x*x - j*j
            b = 2*j*x
            c = x*x + j*j

            n = a+b+c

            if n == y:
                break
        x += 1
    status = c*c
    print(status,end=' ')
