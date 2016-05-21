# solution to https://www.hackerrank.com/challenges/bear-and-steady-gene

count = {"A":0, "C":0, "T":0, "G":0}

# every item in d is less than or equal m
def allLessThan(d, m):
    for key in d:
        if d[key] > m:
            return False
    return True

n = int(raw_input())
s = raw_input()
for i in range(n):
    count[s[i]] = count[s[i]] + 1

start = 0
end = 1

while not allLessThan(count, n/4):
    count[s[end-1]] = count[s[end-1]] - 1
    end = end + 1

opt = end - start - 1
while end <= n:
    if(allLessThan(count, n/4)):
        if end - start - 1 < opt:
            opt = end - start - 1
        count[s[start]] = count[s[start]] + 1
        start = start + 1
    else:
        count[s[end-1]] = count[s[end-1]] - 1
        end = end + 1

print(opt)
