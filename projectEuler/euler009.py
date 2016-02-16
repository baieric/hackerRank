#!/bin/python3

import sys

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    max = 0
    for a in range(3,n):
        b = (n*(n - 2*a)) / (2*(n-a))
        c = n - a - b
        if(a + b + c == n and a > 0 and b > 0 and c > 0 and b == int(b)):
            if(max < a * b * c):
                max = a * b * c
    if(max == 0):
        print("-1")
    else:
        print(str(int(max)))
