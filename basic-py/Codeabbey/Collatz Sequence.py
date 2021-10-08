loop = int(input())
y = [int(i) for i in input().split()]
for a in y:
    x = 0
    a = int(a)
    while a != 1:
        if a%2 == 0:
            a = a/2
            x += 1
        else:
            a = 3*a+1
            x += 1

    print (x,' ',sep='')