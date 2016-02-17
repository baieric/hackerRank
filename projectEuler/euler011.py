#!/bin/python3

import sys

arr = []
for i in range(20):
    row = [int(x) for x in input().strip().split(' ')]
    arr.append(row)

maxVal = 0
for i in range(20):
    for j in range(17):
        val1 = arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3]
        val2 = arr[j][i] * arr[j+1][i] * arr[j+2][i] * arr[j+3][i]
        maxVal = max([maxVal, val1, val2])

for i in range(17):
    for j in range(17):
        val1 = arr[i][j] * arr[i+1][j+1] * arr[i+2][j+2] * arr[i+3][j+3]
        val2 = arr[i][19-j] * arr[i+1][18-j] * arr[i+2][17-j] * arr[i+3][16-j]
        maxVal = max([maxVal, val1, val2])

print(maxVal)
