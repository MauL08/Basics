loop = int(input())
for i in range(loop):
    a,b,c = [int(a) for a in input().split()]
    aritmatic = c/2*(2*a+(c-1)*b)
    print(int(aritmatic),' ',sep=' ')