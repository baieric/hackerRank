# solution to https://www.hackerrank.com/challenges/common-child

a = input()
b = input()
n = len(a) + 1
t = [[0 for x in range(n)] for y in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if a[i-1] == b[j-1]:
            t[i][j] = t[i-1][j-1] + 1
        else:
            t[i][j] = max(t[i-1][j], t[i][j-1])
print(t[n-1][n-1])
