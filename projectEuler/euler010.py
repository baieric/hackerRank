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

t = int(input().strip())
inp = []
for i in range(t):
    n = int(input().strip())
    inp.append(n)
s = sorted(inp)

ans = {}
sum = 0
x = 0
for i in primeList:
    toBreak = False
    while(i > s[x]):
        ans[s[x]] = sum
        x = x + 1
        if(x >= t):
            toBreak = True
            break
    if(toBreak):
        break
    sum = sum + i

for i in range(t):
    print(ans[inp[i]])
