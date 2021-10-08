import math

P,bunga,L = [int(x) for x in input().split()]
R = (bunga/100)/12
M = P*(R*math.pow(1+R,L))/((math.pow(1+R,L))-1)

print(round(M,0))