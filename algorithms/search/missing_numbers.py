# Solution to https://www.hackerrank.com/challenges/missing-numbers

n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
b = [int(x) for x in input().split()]

d = dict()
for i in b:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

for i in a:
    if d[i] > 1:
        d[i] = d[i] - 1
    else:
        d.pop(i)

l = sorted(list(d.keys()))
print(' '.join(str(x) for x in l))
