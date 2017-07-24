cost = 0;
t = int(input());

def dfs(i, nodes):
    nodes += 1;
    for k in range(0, len(adjlist[i])):
        if(visited[adjlist[i][k]] == False):
            nodes += True;
            visited[adjlist[i][k]] = True;
            dfs(adjlist[i][k], nodes);
    return nodes;

for i in range(0, t):
    n, m, cr, cl = input().split();
    n, m, cr, cl = [int(n), int(m),int(cr), int(cl)];
    adjlist = [[] for k in range(n+1)];
    visited = [False for s in range(n)];
    for j in range(0, m):
        u, v = input().split();
        u, v = [int(u), int(v)];
        adjlist[u].append(v);
        adjlist[v].append(u);
    for k in range(0, n):
        if(visited[k] == False):
            node = dfs(k, 0);
        if cl>cr:
            cost += cl*node;
        else:
            x=node-1;
            cost += cl + cr*x;

print(cost);
