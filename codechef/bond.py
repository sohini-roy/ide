t = int(input());

for i in range(0,t):
    n = int(input());
    small = n-1;
    for j in range(0,57):
        power = 2**j
        if((abs(n - power))< small):
            small = abs(n - power);
            if(power > n):
                break;

    print(small);
