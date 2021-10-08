loop = int(input())
for i in range(loop):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = str(c)
    if c == 'n':
        status = a%(b+1)
    elif c == 'i':
        status = a%(b+1)-1
    if status < 0:
        status = b
    print(status,end=' ')