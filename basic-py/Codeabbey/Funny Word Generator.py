Vowel = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','w','x','z']
Const = ['a','e','i','o','u']
A = 445
C = 700001
M = 2097152

a,b = input().split()
a = int(a)
b = int(b)

for i in range(a):
    c = [int(x) for x in input().split()]
    for j in c:
        j = int(j)
        for k in range(j):
            b = ((b*A)+C) % M
            if k % 2 == 0:
                kata = b % 19
                status = Const[kata]
            elif k % 2 != 0:
                kata = b % 5
                status = Vowel[kata]
        print(status,' ',sep='')
