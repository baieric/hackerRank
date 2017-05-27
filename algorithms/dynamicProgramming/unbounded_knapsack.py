# Solution to https://www.hackerrank.com/challenges/unbounded-knapsack

t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    ans = 0
    # cache[i]: whether i can be made using elements in A
    cache = [False for x in range(k+1)]
    # base case: 0 can be made by selecting no items in A
    cache[0] = True
    # Induction: i can be made if an element in A, j, exists such that
    # i - j >= 0 and i-j can be made
    for i in range(1, k+1):
        for j in a:
            if i - j >= 0 and cache[i-j]:
                cache[i] = True
                ans = i
    print(ans)
