#!/bin/python3

import sys

t = int(input().strip())
for i in range(t):
    n= int(input().strip())
    product = 1
    for j in range(2, n+1):
        product = product * j
    val = str(product)
    ans = sum(int(k) for k in val)
    print(ans)
