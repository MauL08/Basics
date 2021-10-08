def josephus(a,b):
    if a == 1:
        return 1
    else:
        return (josephus(a-1,b)+b-1) % a+1

a,b = [int(x) for x in input().split()]
status = josephus(a,b)
print(status)