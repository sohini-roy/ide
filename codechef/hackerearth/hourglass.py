arr = [][];

for i in (0,5):
    for j in (0, 5):
        arr[i][j] = int(input());
least = 0;
for i in (0,5):
    for j in (0, 5):
        sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
        if(sum < least):
            least = sum;

print(least);
