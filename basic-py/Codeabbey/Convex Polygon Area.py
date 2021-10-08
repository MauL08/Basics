#Blm Kelar
loop = int(input())
for i in range(loop):
    a = [int(x) for x in input().split()]

    if i == loop-1:
        num +=  (a*b[0])-(b*a[0])
    else:
        num += (x[i] * y[i + 1]) - (y*x[i+1])