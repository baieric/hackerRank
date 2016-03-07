#!/bin/python3

import sys

t = int(input().strip())
for i in range(t):
    triangle = []
    n= int(input().strip())
    for j in range(n):
        row = input().strip().split(' ')
        for k in range(len(row)):
            triangle.append(int(row[k]))
    maxSum = triangle
    row = n - 1
    index = len(triangle) - n - 1
    column = row
    while(index >= 0):
        maxSum[index] = triangle[index] + max(maxSum[index + row], maxSum[index+row+1])
        index = index - 1
        column = column - 1
        if(column == 0):
            row = row - 1
            column = row
    print(maxSum[0])
