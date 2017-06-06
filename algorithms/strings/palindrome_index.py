# Solution to https://www.hackerrank.com/challenges/palindrome-index

t = int(input())
for _ in range(t):
    s = input()
    start = 0
    end = len(s) - 1
    ans = -1
    while start < end:
        if s[start] != s[end]:
            left = s[start:end]
            right = s[start+1:end+1]
            if left == left[::-1]:
                ans = end
            elif right == right[::-1]:
                ans = start
            else:
                ans = -1
            break
        start = start + 1
        end = end - 1
    print(ans)
