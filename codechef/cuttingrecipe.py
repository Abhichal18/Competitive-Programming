t = int(input())
from math import gcd
for each_t in range(t):
    l = list(map(int, input().split()))
    g = l[1]
    for i in range(1,len(l)):
        g = gcd(g, l[i])
    for i in range(1,len(l)):
        print(l[i] // g, end=" ")
    print()