#!/bin/python3

import sys

t = int(input().strip())
inp = []
for i in range(t):
    n = int(input().strip())
    inp.append(n)
s = sorted(inp)

ans = {}
sumOfSquares = 0
sum = 0
x = 0
for i in range(1, s[t-1]+1):
    sumOfSquares = sumOfSquares + i * i
    sum = sum + i
    if(i == s[x]):
        ans[s[x]] = sum * sum - sumOfSquares
        x = x + 1

for i in range(t):
    print(ans[inp[i]])
