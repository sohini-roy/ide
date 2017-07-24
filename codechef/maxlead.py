n = int(input());
large = 0;
player = 0;

for i in range(0, n):
    u, v = input().split();
    u ,v = [int(u), int(v)];
    if u>v:
        diff = u - v;
        if diff > large:
            large = diff;
            player = 1;
    else:
        diff = v- u;
        if diff > large:
            large = diff;
            player = 2;

print(large);
print(player);
