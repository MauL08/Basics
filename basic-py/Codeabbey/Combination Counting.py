def combination(n):
    if n <= 1:
        status = 1
    else:
        status = n*combination(n-1)
    return status

loop = int(input())
for i in range(loop):
    a,b = [int(x) for x in input().split()]
    c = abs(combination(a)/(combination(b)*combination(a-b)))
    print(round(int(c),1),end=' ')