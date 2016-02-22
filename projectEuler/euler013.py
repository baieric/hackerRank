#!/bin/python3
import sys

t = int(input().strip())
sum = 0
for i in range(t):
    n = int(input().strip())
    sum = sum + n
print(str(sum)[0:10])
