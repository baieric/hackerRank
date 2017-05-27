# Solution to https://www.hackerrank.com/challenges/maxsubarray

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    first = 0
    second = 0
    maxVal = a[0]
    maxEncountered = 0

    for i in a:
        maxEncountered = max(maxEncountered + i, 0)
        first = max(maxEncountered, first)

        if i > 0:
            second = second + i
        maxVal = max(maxVal, i)

    if maxVal < 0:
        second = maxVal
        first = maxVal

    print(str(first) + " " + str(second))
