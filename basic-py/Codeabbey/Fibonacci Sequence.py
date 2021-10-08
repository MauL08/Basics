import math

loop = int(input())
gratio = 1.6180339887
for i in range(loop):
    a = int(input())
    fibo = (math.log(a)+math.log(5)/2)/math.log(gratio)

    print(round(fibo),' ',sep='')