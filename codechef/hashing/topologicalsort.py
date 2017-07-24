n = int(input())
m = int(input())
adj = [[] for value in range(0, n)]
visited = [False for value in range(0, n)]

for value in range(0, m):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    adj[u].append(v)

def toposort(i):
    visited[i] = True
    for node in adj[i]:
        if visited[node] == False:
            toposort(node)

    stack.append(node)
    return stack

def topoOrder():
    stack = []
    for i in range(0, n):
        if visited[i] == False:
            topoSort(i)

    print(list(stack))
