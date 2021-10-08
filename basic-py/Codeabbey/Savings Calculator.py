loop = int(input())
for i in range(loop):
    inc = 0
    S,R,P = [int(x) for x in input().split()]

    while S < R:
        total = (S*(P/100))
        S += total
        inc += 1

    print(inc,' ',sep='')