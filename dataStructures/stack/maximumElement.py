# solution to https://www.hackerrank.com/challenges/maximum-element
n = int(input())
stack = []
size = 0
for i in range(n):
    cmd = input().split(" ")
    if cmd[0] == '1':
        val = int(cmd[1])
        if size == 0:
            item = [val, val]
        else:
            m = max(val, stack[size-1][1])
            item = [val, m]
        stack.append(item)
        size += 1
    if cmd[0] == '2':
        stack.pop()
        size -= 1
    if cmd[0] == '3':
        print(stack[size-1][1])
