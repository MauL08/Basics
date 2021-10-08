loop = int(input())
P1 = ["SP","PR","RS"]
P2 = ["PS","RP","SR"]
for i in range(loop):
    p_1 = 0
    p_2 = 0
    a = [str(a) for a in input().split()]
    for j in a:
        if j in P1:
            p_1 += 1
        if j in P2:
            p_2 += 1
    if p_1 > p_2:
        status = 1
    else:
        status = 2

    print(status,' ',sep='')
