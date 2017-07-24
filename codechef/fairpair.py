T = int(input());

while(t--):
    n = int(input());
    sub = [];
    assign = [];
    for i in range(0,n):
        sub[i] = int(input());
    for i in range(0,n):
        assign[i] = int(input());

    sub.sort();
    assign.sort();
    count = 0;
    if(sub[n] == assign[0]):
        ++count;
    for i in range (0, t):
        if(sub[i] == assign[i+1]):
            ++count;
        print(i+1);
        
