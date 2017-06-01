# Solution to https://www.hackerrank.com/challenges/sherlock-and-pairs

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    seen = dict()
    for i in a:
        if i in seen:
            seen[i] = seen[i] + 1
        else:
            seen[i] = 1
    pairs = 0
    for k,v in seen.items():
        pairs = pairs + (v * (v-1))
    print(pairs)
