loop = int(input())
a = [int(i) for i in input().split()]
b = 0
for i in a:
    b = int(b)
    b = (b+i)*113

    if b > 10000007:
        b %= 10000007

print(b)