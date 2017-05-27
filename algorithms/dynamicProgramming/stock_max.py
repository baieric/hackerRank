#!/bin/python3

import sys

# Solution to https://www.hackerrank.com/challenges/stockmax

t = int(input().strip())
for a0 in range(t):
    N = int(input().strip())
    prices = list(map(int, input().strip().split(' ')))

    maxPrice = 0
    profit = 0
    for i in reversed(prices):
        if i > maxPrice:
            maxPrice = i
        else:
            profit = profit + maxPrice - i
    print(profit)
