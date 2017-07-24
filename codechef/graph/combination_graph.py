n, p = input().split()
n, p = [int(n), int(p)]
edgeu = list()
edgev = list()
adj = [[] for i in range(0, n)]
visited = [0 for i in range(0, n)]
cluster = [0 for i in range(0, n)]
pair = 0

def dfs(list, node):
    node += 1;
    for i in range(0, len(list)):
        if(visited[i] == 0):
            visited[i] = 1;
            dfs(adj[i], node);
    return node;

for i in range(0, p):
    u, v = input().split()
    u, v = [int(u), int(v)]
    edgeu.append(u)
    edgev.append(v)

for i in range(0, len(edgeu)):
        u = edgeu[i]
        v = edgev[i]
        adj[u].append(v);

for j in range(0, n):
    cluster[i] = dfs(adj[j], 0);

for i in range(0, n):
    for j in range(i+1, n):
        pair = pair + cluster[i]*cluster[j];

print(pair);
