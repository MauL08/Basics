loop = int(input())
for i in range(loop):
    a = [int(x) for x in input().split()]
    avr = sum(a)/(len(a)-1)
    print(round(avr),' ',sep='')