inf = 10**9
q = int(input())
queue = []
dist = 0

def bfs(s,d,graph,visited):
    visited[s] = 1
    for i in range(0, len(graph)):
        node = graph[i]
        visited[node] = 1
        queue.append(node)
        prev[node] = s
    for i in range(0, len(queue)):
        s = queue[i]
        graph = adj[s]
        bfs(s, d, graph, visited)

for i in range(0, q):
    n,m = int(input().split());
    adj = [[] for k in range(0, n)]
    for j in range(0,m):
        u = int(input());
        v = int(input());
        adj[u].append(v);
        adj[v].append(u);
    s = int(input());
    prev = [[] for b in range(0,n)]
    visited = [0 for a in range(0, n)]
    queue.append(adj[s]);
    for c in range(0, n-1):
        if c==s:
            continue
        else:
            print(bfs(s,i,adj[s],visited))
