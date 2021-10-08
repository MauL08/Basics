secret,b = input().split()
secret = str(secret)
b = int(b)
number = [str(x) for x in input().split()] #Value
for i in range(b):
    bulls = 0
    cows = 0
    for j in range(4):
        if number[i][j] == secret[j]:
            bulls += 1
        elif number[i][j] in secret:
            cows += 1
    print(bulls,cows,sep='-',end=' ')