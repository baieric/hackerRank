# Solution to https://www.hackerrank.com/challenges/fibonacci-modified

a = [int(x) for x in input().split()]
cache = [a[0], a[1]]
n = a[2]

for i in range(2, n):
    val = cache[i-2] + (cache[i-1] * cache[i-1])
    cache.append(val)

print(cache[n-1])
