loop = int(input())
a = 0
b = 1
fibo = [int(x) for x in input().split()]
for i in fibo:
    inc = 1
    for j in range(0, 10000):
        c = a+b

        a = b
        b = c

        inc += 1

        a = a % i
        b = b % i

        if b % i == 0:
            break

    print(inc,' ',sep='')