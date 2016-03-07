#!/bin/python3

import sys
from functools import reduce
from operator import mul
from fractions import Fraction

def nCk(n,k):
  return int(reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))

t = int(input().strip())
for i in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    print(nCk(n+m, n)%(10**9+7))
