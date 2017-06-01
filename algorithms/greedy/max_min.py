# Solution to https://www.hackerrank.com/challenges/angry-children

n = int(input())
k = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

s = sorted(a)
begin = 0
end = k - 1
trough = -1

while end < n:
    if trough == -1:
        trough = s[end] - s[begin]
    else:
        trough = min(trough, s[end] - s[begin])

    begin = begin + 1
    end = end + 1

print(trough)
