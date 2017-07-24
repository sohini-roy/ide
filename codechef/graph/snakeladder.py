t = int(input())

def game(start,count,al_len):
    if(start < 100):
        snake  = []
        for i in range(start, al_len):
            if(al[i][2] == 1):
                nextstep = al[i][0] - start
                sixes = nextstep/6
                rest = nextstep%6
                start = al[i][1]
                break
            else :
                snake.append(al[i][0])
        
    else:
        return count

for i in range (0, t):
    al =[]
    edge=list()
    n=int(input())
    count = 0
    for j in range (0, n):
        u, v = input().strip().split(' ')
        u, v = [int(u), int(v)]
        edge.append(u)
        edge.append(v)
        edge.append(1)
        al.append(edge)
    m = int(input())
    for j in range (0, m):
        u, v = input().strip().split(' ')
        u, v = [int(u), int(v)]
        edge.append(u)
        edge.append(v)
        edge.append(0)
        al.append(edge)
    al = sorted(al,key=lambda x: x[0])
    l = len(al)
