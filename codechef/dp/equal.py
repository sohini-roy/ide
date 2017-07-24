t = int(input())

def inc(ar, n, k):
    for j in range(0, n-1):
        ar[j] += k
    ar.sort()
    return ar

def equalise(ar, count, n):
    if ar[0] is not ar[n-1]:
        diff = ar[n-1] - ar[0]
        if diff >= 5:
            ar = inc(ar, n, 5)
            count += 1
        else :
            if diff >= 2:
                ar = inc(ar, n, 2)
                count += 1
            else:
                ar = inc(ar, n, 1)
                count += 1
        return equalise(ar, count, n)
    else:
        return count

for i in range(0,t):
    n= int(input())
    ar = list(map(int, input().strip().split(' ')))
    ar.sort()
    count = equalise(ar, 0, n)
    print(count)
