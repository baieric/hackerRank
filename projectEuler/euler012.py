#!/bin/python3

import sys
primes = [True for i in range(10**6 + 1)]
primes[1] = False
for i in range(2, 10**3 + 1):
    if(primes[i]):
        for j in range(i*i, 10**6 + 1, i):
            primes[j] = False

primeList = [2]
for i in range(3, 10**6 + 1, 2):
    if(primes[i]):
        primeList.append(i)

dict = {}
def divisors(n):
    if(n in dict):
        return dict[n]
    copy = n
    num = 1
    for i in primeList:
        if(n == 1):
            dict[copy] = num
            return num
        d = n/i
        x = 0
        while(n == int(d) * i):
            n = d
            d = n/i
            x = x + 1
        num = num * (x + 1)

t = int(input().strip())
inp = []
for i in range(t):
    n = int(input().strip())
    inp.append(n)
s = sorted(inp)

ans = {}
x = 0

triangle = 1
div = 1
while (x < t):
    while(div <= s[x]):
        triangle = triangle + 1
        if(triangle/2 == int(triangle/2)):
            term1 = triangle/2
            term2 = triangle + 1
        else:
            term1 = triangle
            term2 = (triangle + 1) / 2
        div = divisors(term1) * divisors(term2)
    ans[s[x]] = triangle * (triangle +1) / 2
    x = x + 1

for i in range(t):
    print(int(ans[inp[i]]))
