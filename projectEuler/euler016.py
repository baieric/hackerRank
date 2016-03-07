#!/bin/python3

import sys

t = int(input().strip())
for i in range(t):
    n= int(input().strip())
    val = str(2**n)
    ans = sum(int(k) for k in val)
    print(ans)
