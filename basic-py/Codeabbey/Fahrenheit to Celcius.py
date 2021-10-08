suhu = [int(x) for x in input().split()]
x = suhu[1:]
for i in x:
    FtoC = 5*(i-32)/9 + 0.5
    print(round(int(FtoC)),end=' ')