t = int(input())

# def maxexp(ar, s, p, i, length):
#     if i < length:
#         if i == 0:
#             s += 1
#         else:
#             if i == (length - 1) :
#                 p += s*ar[i]
#                 return p
#             else:


for i in range (0, t):
    n = int(input())
    #enter space-separated elements into array of size n
    ar = [int(j) for j in input().strip().split()]
    ar.sort()
    s = n
    p1 = s * ar[n-1]
    p2 = (sum(ar) - ar[0])*2
    if p1 > p2:
        print(p1)
    else:
        print(p2)
    # res = maxexp(ar, 1, 0, 0, len(ar))
    # print(res)
