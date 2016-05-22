# slow, but sufficient if you do not need to compute many primes
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

# works if you call this for n = 2, 3, ...
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

# even better, sieve the primes
primes = [True for i in range(10**6 + 1)]
primes[1] = False
for i in range(2, 10**3 + 1):
    if(primes[i]):
        for j in range(i*i, 10**6 + 1, i):
            primes[j] = False

primeList = [2]
for i in range(3, 10**6 + 1, 2):
    if(primes[i]):
        primeList.append(i)

# import a bunch of stuff to do n choose k :)
import sys
from functools import reduce
from operator import mul
from fractions import Fraction
def nCk(n,k):
  return int(reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))

# set up stuff, just to save time
t = int(input())
for t0 in range(t):
    n = int(input())
    ar = [int(x) for x in input().split(" ")]
    table = [[0 for x in range(n)] for y in range(n)]
