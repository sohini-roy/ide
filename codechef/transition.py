t = int(input())
def getDistance(x,y):
    distance = 0
    diagonals = min(abs(x[0]-y[0]),abs(x[1]-y[1]))
    distance += diagonals
    distance += abs(x[0]-y[0]) - diagonals
    distance += abs(x[1]-y[1]) - diagonals
    return distance
def getNeighbors(x,maxrow,maxcol):
    ne = []
    if x[0] - 1 >= 0:
        ne.append((x[0]-1,x[1]))
    if x[0] + 1 < maxrow:
        ne.append((x[0]+1,x[1]))
    if x[1] - 1 >= 0:
        ne.append((x[0],x[1]-1))
    if x[1] + 1 < maxcol:
        ne.append((x[0],x[1]+1))
    if x[0] - 1 >= 0 and x[1]-1 >= 0:
        ne.append((x[0]-1,x[1]-1))
    if x[0] - 1 >= 0 and x[1]+1 <maxcol:
        ne.append((x[0]-1,x[1]+1))
    if x[0] + 1 < maxrow and x[1]-1 >= 0:
        ne.append((x[0]+1,x[1]-1))
    if x[0] + 1 < maxrow and x[1]+1 < maxcol:
        ne.append((x[0]+1,x[1]+1))
    return ne

for test in range(t):
    maxrow,maxcol = list(map(int,input().split(' ')))
    a = []
    for i in range(maxrow):
        a.append(list(map(int,input().split(' '))))
    maxVal = -1
    maxList = []
    for i in range(maxrow):
        for j in range(maxcol):
            if a[i][j] > maxVal:
                maxVal = a[i][j]
                maxList = []
            if a[i][j] == maxVal:
                maxList.append((i,j))
    reached = []
    for i in range(maxrow):
        reached.append([])
        for j in range(maxcol):
            if a[i][j] == maxVal:
                reached[i].append(True)
            else:
                reached[i].append(False)

    left = (maxrow*maxcol) - len(maxList)
    maxDistance = 0

    while(left > 0):
        newMax = []
        for i in range(len(maxList)):
            maxEle = maxList[i]
            nes = getNeighbors(maxEle,maxrow,maxcol)
            for k in range(len(nes)):
                ne = nes[k]
                if not reached[ne[0]][ne[1]]:
                    reached[ne[0]][ne[1]] = True
                    left -= 1
                    newMax.append(ne)
        maxDistance += 1
        maxList = newMax
        # print(maxList)
    print(maxDistance)
