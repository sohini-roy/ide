#kangaroo jump:

# x1,v1,x2,v2 = input().strip().split(' ')
# x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)];
#
# n = abs(x1 - x2)/abs(v1 - v2);
# if (n).is_integer():
#     if x1+v1*n == x2+v2*n :
#         print('yes');
#     else:
#         print('no');
#
#divisibility
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int, input().strip().split(' ')));

def start(x, k):
    for i in range(1, n):
        if a.index(i*abs(k - x)) :
            index = a.index(i*(k - first));
            return index;
        else:
            continue;

a.sort();
count = 0;
# i = a.index(k - first);
for i in range(0, n):
    index = start(a[i]);
    if(index):
        for j in range (index, n):
            if !((a[i]+a[j])/k):
                count += 1;
