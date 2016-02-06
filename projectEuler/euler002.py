#!/bin/python3

import sys

t = int(input().strip());
for i in range(t):
    n = int(input().strip())
    first = 5
    second = 8
    sum = 2
    while(second < n):
        if (second % 2 == 0):
            sum = sum + second
        tmp = first
        first = second
        second = second + tmp
    print(sum)
