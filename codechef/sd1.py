T = int(input())

for i in range(0,T):
    res = "no"
    n, m = input().split(' ');
    n = int(n);
    m = int(m)
    for j in range(0,m):
        u, v = input().split(' ');
    if(n%2):
        res = "no"
    else:
        res = "yes"

    print (res)
