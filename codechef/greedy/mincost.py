n = int(input())
ar = list(map(int, input().strip().split(' ')))
ar.sort()
w = ar[0]
price = 1
for i in range(0,n):
    if ar[i] > (w+4):
        w = ar[i]
        price += 1
print(price)
