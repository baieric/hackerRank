#!/bin/python3

import sys

primes = [37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]

def lpf(x):
    for n in primes:
        y = int(x/n)
        if(y * n == x):
            return n

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    ans = 1
    x = 2
    while(x <= n):
        if(ans % x != 0):
            y = lpf(x)
            ans = ans * y
        x = x + 1
    print(ans)
