def dadu(x):
    return (x % 6) + 1

loop = int(input())
for i in range(loop):
    a,b = input().split()
    a = int(a)
    b = int(b)

    p = dadu(a)
    q = dadu(b)
    r = p+q

    print(round(int(r),0),' ',sep='')