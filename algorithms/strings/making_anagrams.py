a = input()
b = input()
x = {}
y = {}

for ch in a:
    if ch in x:
        x[ch] = x[ch] + 1
    else:
        x[ch] = 1

for ch in b:
    if ch in y:
        y[ch] = y[ch] + 1
    else:
        y[ch] = 1

ans = 0

for key, value in x.items():
    if key in y:
        if value > y[key]:
            ans = ans + value - y[key]
    else:
        ans = ans + value

for key, value in y.items():
    if key in x:
        if value > x[key]:
            ans = ans + value - x[key]
    else:
        ans = ans + value

print(ans)
