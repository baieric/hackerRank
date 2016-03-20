import sys

n = int(input().strip())
names = []
for i in range(n):
    name = input().strip()
    names.append(name)
sortedNames = sorted(names)
nameDict = {}
for i in range(len(sortedNames)):
    nameDict[i+1] = sortedNames[i]
position = dict((y,x) for x,y in nameDict.items())
q = int(input().strip())
for i in range(q):
    name = input().strip()
    score = 0
    for c in range(len(name)):
        score = score + ord(name[c]) - ord('A') + 1
    score = score * position[name]
    print(score)
