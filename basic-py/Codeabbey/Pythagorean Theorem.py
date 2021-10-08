import math
loop = int(input())
for i in range(loop):
    a,b,c = [int(a) for a in input().split()]
    seq = math.sqrt(a*a + b*b)

    if c < seq:
        status = 'A'
    if c > seq:
        status = 'O'
    if c == seq:
        status = 'R'

    print(status,' ',sep='')