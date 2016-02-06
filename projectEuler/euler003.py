#!/bin/python3

import sys
import math

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    for i in range(1, n):
        x = int(n / i)
        if (x * i != n):
            continue
        if (isPrime(x)):
            print(x)
            break
        
