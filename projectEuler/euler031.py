# solution to https://www.hackerrank.com/contests/projecteuler/challenges/euler031

p = [1, 2, 5, 10, 20, 50, 100, 200]
t = int(input())
a = []
hi = 0
for t0 in range(t):
    n = int(input())
    a.append(n)
    hi = max(hi, n)

cache = [1 for x in range(hi+1)]

for i in range(1, len(p)):
    for j in range(p[i], hi+1):
        cache[j] = cache[j] + cache[j-p[i]]
for i in a:
    print(cache[i] % (10**9 + 7))
