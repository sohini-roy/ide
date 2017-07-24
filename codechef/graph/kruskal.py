n, m = input().split()
n, m = [int(n),int(m)]
visited =[0 for i in range (0,n)]
path = []

for i in range(0, m):
    weight = []
    x, y, r = input().split()
    x,y,r = [int(x),int(y),int(r)]
    weight.append(x)
    weight.append(y)
    weight.append(r)
    path.append(weight)

path = sorted(path,key=lambda x: x[2])
print(path)
count = 0
total_weight = 0
j= 0
print('entering while')
while(count < n):
    print('entered while')
    x = path[j][0]
    y = path[j][1]
    if visited[x] or visited[y]:
        total_weight += path[j][2]
        if visited[x] == 0:
            visited[x] = 1
            count += 1
        if visited[y] == 0:
            visited[y] = 1
            count += 1

print(total_weight)
