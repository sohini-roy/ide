n, d= input().split(' ');
list = [];
result = [];
n = int(n);
d = int(d);

for i in range(0, n):
    list = list(map(int, input().split(' ')));
count = n-1;
while(count > 0):
    temp = list[i];
    if(count - d >= 0):
        result[count - d] = list[count];
    else:
        result[d+count - 1] = list[count];
    count -= 1;
print(list(result));
