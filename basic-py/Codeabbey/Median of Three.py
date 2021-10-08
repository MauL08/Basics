loop = int(input())
for i in range(loop):
    a,b,c = [int(a) for a in input().split()]

    if a>b and a<c or a<b and a>c:
        x = a
    if b>a and b<c or b<a and b>c:
        x = b
    if c>b and c<a or c>a and c<b:
        x = c

    print(x,' ',sep='')