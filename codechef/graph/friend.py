q = int(input())

for i in range (0, q):
    n, m = input().strip().split()
    n, m = [int(n), int(m)]
    visited = [0 for k in range(0, n)]
    value = [0 for k in range(0, n)]
    total = 0
    for j in range(0, m):
        x, y = input().strip().split()
        x, y = [int(x), int(y)]
        if visited[x] == 0 and visited[y] == 0:
            value[x] += 1
            value[y] += 1
        else:
            if (visited[x] == 1 and visited[y] == 0) or (visited[y] == 1 and visited[x] == 0):
                if visited[x] == 1:
                    value[x] += 1
                    for k in range(0, n):
                        if visited[k] == 1:
                            value[k] = value[x]
                else:
                    if visited[y] == 1:
                        value[y] += 1
                        for k in range(0, n):
                            if visited[k] == 1:
                                value[k] = value[y]

    total += sum(value)
    print(total)
