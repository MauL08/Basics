loop = int(input())
b = ['a','i','u','e','o','y']
for i in range(loop):
    x = 0
    a = input()
    for j in a:
        if j in b:
            x+=1
    print(x,' ',sep='')