# Solution to https://www.hackerrank.com/challenges/anagram

t = int(input())
for i in range(t):
    s = input()
    if len(s) % 2 == 1:
        print("-1")
    else:
        s1 = s[:int(len(s)/2)]
        s2 = s[int(len(s)/2):]
        d1 = dict()
        diff = 0
        for c in s1:
            if c in d1:
                d1[c] = d1[c] + 1
            else:
                d1[c] = 1
        for c in s2:
            if c in d1:
                if d1[c] == 0:
                    diff = diff + 1
                else:
                    d1[c] = d1[c] - 1
            else:
                diff = diff + 1
        print(diff)
