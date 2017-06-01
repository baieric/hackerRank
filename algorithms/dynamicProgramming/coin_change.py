#!/bin/python3

# Solution to https://www.hackerrank.com/challenges/coin-change

import sys

def getWays(n, c):
    a = [0 for x in range(n+1)]
    # one way to make change for 0
    a[0] = 1
    for i in c:
        for j in range(i, n+1):
            a[j] = a[j] + a[j-i]
    return a[n]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
