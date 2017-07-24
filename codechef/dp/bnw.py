n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
adj = [[] for i in range (0,n)]
visited = [False for i in range(0, n)]
queue = []
white = []
black = []
#for storing all the components
components =[[] for i in range (0, n)]
queue = []
for i in range(0, m):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    if u is not in white:
        white.append(u)
        black.append(v)
    else:
        white.append(v)
        black.append(u)
    adj[u].append(v)

def retrunComponents():
    current = 1
    for j in range(0, n):
        if visited[j] = True:
            while(adj[j]):
                component[j].append(node)
            
