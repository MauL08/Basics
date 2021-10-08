loop = int(input())
for i in range(loop):
    A,C,M,Xo,N = [int(x) for x in input().split()]
    for j in range(N):
        Xo = ((A*Xo)+C) % M

    print(Xo,' ',seq='')