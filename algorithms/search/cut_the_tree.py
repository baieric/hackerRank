import sys

class Node(object):
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
        self.total = 0

    def add(self, child):
        self.children.append(child)

    def setSum(self, total):
        self.total = total

n = int(input())
a = [-1]
total = 0
for x in input().split():
    total = total + int(x)
    a.append(Node(int(x), []))

for _ in range(n-1):
    u, v = [int(x) for x in input().split()]
    a[u].add(v)

def setSum(node):
    ans = a[node].value
    for child in a[node].children:
        ans = ans + setSum(child)
    a[node].setSum(ans)
    return ans

setSum(1)

trough = sys.maxsize
for i in range(1, n+1):
    for child in a[i].children:
        if total - a[child].total < trough:
            trough = abs(total - a[child].total - a[child].total)
print(trough)
