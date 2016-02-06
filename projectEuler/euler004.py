#!/bin/python3

import sys

def getPalindrome(half):
    palindrome = half * 1000
    multi = 100
    while (half > 0):
        x = half % 10
        half = int(half/10)
        palindrome = palindrome + x * multi
        multi = multi / 10
    return int(palindrome)

def largestPalindrome(n):
    half = int(n/1000)
    palindrome = getPalindrome(half)
    while(palindrome > n):
        half = half - 1
        palindrome = getPalindrome(half)
    return palindrome

def isProduct(n):
    for i in range(100, 1000):
        x = int(n/i)
        if(x < 1000 and x*i == n):
            return True
    return False

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    x = largestPalindrome(n)
    half = int(x/1000)
    while(half > 100):
        if(isProduct(x)):
            print(x)
            break
        half = half - 1
        x = getPalindrome(half)
