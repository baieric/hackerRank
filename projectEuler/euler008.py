#!/bin/python3

import sys

t = int(input().strip())
for i in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    dig = list(int(d) for d in num)
    max = 0
    for j in range(n-k+1):
        ans = 1
        for l in range(k):
            ans = ans * dig[j + l]
        if(ans > max):
            max = ans
    print(max)
