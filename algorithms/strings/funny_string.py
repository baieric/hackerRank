def is_funny(s):
    l = len(s)
    for i in range(1, l):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[l-i-1]) - ord(s[l-i])):
            return False
    return True

n = int(input())
for _ in range(n):
    s = input()
    if is_funny(s):
        print("Funny")
    else:
        print("Not Funny")
