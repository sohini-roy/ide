m, w, p, n = input().split();
m, w, p, n = [int(m), int(w), int(p), int(n)];
count = m*w;
turns = 1;
while(count <= n):
    inc = count/2;
    count = count%2;
    if m > w:
        w += inc;
    else:
        m += inc;
    count += m*w;
    turns += 1;

print(turns);
