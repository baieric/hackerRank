#!/bin/python3

# Solution to https://www.hackerrank.com/challenges/string-construction

import sys


n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    p = ""
    i = 0
    cost = 0
    sub = ""
    while i < len(s):
        if s[i] not in p:
            cost = cost + 1
            p = p + sub + s[i]
            sub = ""
        else:
            sub = sub + s[i]
        i = i + 1
    print(cost)
