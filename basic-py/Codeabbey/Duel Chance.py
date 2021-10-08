loop = int(input())
for i in range(loop):
    a,b = input().split()
    a = int(a)
    b = int(b)

    chance = a/(1-(1-a/100)*(1-b/100))

    print(round(chance),' ',sep='')