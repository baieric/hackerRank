# solution to https://www.hackerrank.com/contests/projecteuler/challenges/euler034

n = int(input())
fac =[1]
for i in range(1, 10):
    fac.append(i*fac[i-1])

ans = 0
index = 10
while index < n:
    num = index
    sumF = 0
    while num > 0:
        d = num % 10
        num = num // 10
        sumF += fac[d]
    div = sumF // index
    if div > 0 and div == sumF / index:
        ans += index
    index += 1
print(ans)
