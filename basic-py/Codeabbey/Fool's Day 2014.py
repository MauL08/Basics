loop = int(input())
for i in range(loop):
    sum = 0
    a = input().split()
    for j in a:
        j = int(j)
        j = j**2
        sum += j
    print(sum,' ',sep='')