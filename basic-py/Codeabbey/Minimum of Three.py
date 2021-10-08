loop = int(input())
for i in range(loop):
    a,b,c = [int(a) for a in input().split()]

    if a<b :
        if a<c :
            x = a
        else :
            x = c
    else :
        if b<c :
            x = b
        else :
            x = c

    print(x,' ', sep='')