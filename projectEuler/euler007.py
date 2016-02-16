#!/bin/python3

import sys

primes = []

def isPrime(n):
    if n==2 or n==3:
        primes.append(n)
        return True
    if n<2: return False
    for i in primes:
        if n%i==0:
            return False
    primes.append(n)
    return True

t = int(input().strip())
arr = []
for i in range(t):
    n = int(input().strip())
    arr.append(n)

s = sorted(arr)
x = 0
num = 2
while(x < s[t-1]):
    if(isPrime(num)):
        x = x + 1
    num = num + 1

for i in range(t):
    print(primes[arr[i]-1])
