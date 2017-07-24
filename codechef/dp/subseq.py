t = int(input())
ar = []
l = 0

def check(sumleft, sumright,i,count):
    if i < l:
        print('l7')
        print(l)
        if sumleft == sumright:
            print('l10')
            count += 1
            print(count)
            sumleft = 0
            print('l14')
            check(sumleft, sumright, i,count)
            return count
        else:
            print('l17')
            sumleft += ar[i]
            print(sumleft)
            sumright -= ar[i]
            print(sumright)
            i += 1
            print(i)
            print('l24')
            check(sumleft, sumright, i,count)


for i in range(0,t):
    n = int(input())
    ar = [int(j) for j in input().strip().split()]
    l = len(ar)
    sumleft = 0
    sumright = sum(ar)
    res = check(sumleft,sumright, 0,0)
    print(res)
