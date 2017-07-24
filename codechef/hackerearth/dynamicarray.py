seqlist = [];
lastans = 0;
n ,q = input().split(' ');
q = int(q);
n = int(n);

for j in range(0,q):
    new = [];
    for z in range(0,n):
        seqlist.append(new);
    k, x, y = input().split(' ');
    x = int(x);
    y = int(y);
    k = int(k);
    i = (x^lastans)%n;
    print(i);
    if(k == 1):
        seqlist[i].append(y);
        print(list(seqlist));
    else:
        l = len(seqlist[i]);
        print(l);
        lastans = seqlist[i][y%l];
    print('\n');
    print(lastans);
