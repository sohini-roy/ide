q = int(input())
for i in range(0, q):
    a,b,c,d = input().strip().split(' ')
    a,b,c,d = [int(a),int(b),int(c),int(d)]
    count = 0;
    x=1
    while(x <= c):
        y = 1
        while(y <= d):
            lhs = x*(x - a)
            rhs = y*(b - y)
            if lhs == rhs:
                count += 1
            y += 1
        x += 1
    print(count)
