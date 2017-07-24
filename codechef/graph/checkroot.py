q = int(input())

for i in range(0, q):
    n = int(input())
    roots =[[] for j in range (0, n) ]
    for j in range(0, n-1):
        u,v = input().strip().split(' ')
        u,v = [int(u), int(v)]
        root[v].append(u)
    g, k = input().strip().split(' ')
    g,k = [int(g),int(k)]
    guess = [[] for k in range(0,g)]
    visited  = [0 for k in range(0,n)]
    for k in range(0,q):
        u,v = input().strip().split(' ')
        u,v = [int(u), int(v)]
        if root[v][0] == u:
            if visited[u] == 0:
                count += 1
                visited[u] = 1

    print(count,'/',n)
