n,k,m = input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
#adj list for all nodes
adj = [[] for j in range(0, n)]
adjlist = list()

def move(index):
    for j in range(index, m):
        a[index] = a[index + 1]

def addadjnode(u, v):
    for x in range(0, len(adj[u])):
        node = adj[u][x]
        if v not in adj[node]:
            adj[node].append(v)
    for x in range(0, len(adj[v])):
        node = adj[v][x]
        if v not in adj[node]:
            adj[node].append(u)

for i in range(k):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]
    if x not in adj[y]:
        adj[y].append(x)
    if y not in adj[x]:
        adj[x].append(y)
    addadjnode(x, y)

a = list(map(int, input().strip().split(' ')))

x
for i in range(0, m):
