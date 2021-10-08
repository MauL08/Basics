loop = int(input())
skip = 0
swap = 0
a = [int(x) for x in input().split()]
size = len(a)
for j in range(0,size):
    temp = 0
    for k in range(0,size-j-1):
        if a[k] > a[k+1]:
            a[k],a[k+1] = a[k+1],a[k]
            swap += 1
        skip += 1
        swap += temp
print(swap,"",skip,end=' ')
