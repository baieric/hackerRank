q = int(input())
for a0 in range(q):
    n, m = [int(x) for x in input().split()]
    g = [[0 for x in range(n+1)] for y in range(n+1)]

    for a1 in range(m):
        u, v = [int(x) for x in input().split()]
        g[u][v] = 1
        g[v][u] = 1

    s = int(input())
    dist = [-1 for x in range(n+1)]
    dist[s] = 0
    traversed = [False for x in range(n+1)]
    traversed[s] = True

    queue = [s]
    current = 1
    while len(queue) > 0:
        u = queue.pop(0)
        for v in range(n+1):
            if g[u][v] == 1 and traversed[v] == False:
                dist[v] = dist[u] +1
                traversed[v] = True
                queue.append(v)

    for i in range(1, n+1):
        if dist[i] > 0:
            print(str(dist[i] * 6) + " ", end='')
        elif i != s:
            print("-1 ", end='')
    print("")
