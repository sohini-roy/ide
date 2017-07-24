m = int(input().strip())
ar1 = [int(i) for i in input().strip().split()]
ar2 = [int(i) for i in input().strip().split()]
arr1 = []
arr2 = []

for i in range(0, m):
    x = []
    x.append(ar1[i])
    x.append(i)
    arr1.append(x)
    x = []
    x.append(ar2[i])
    x.append(i)
    arr2.append(x)

arr1 = sorted(arr1,key=lambda x: x[0])
arr2 = sorted(arr2,key=lambda x: x[0])
if arr1[0][1] == arr2[0][1]:
    a = arr1[0][0] + arr2[1][0]
    b = arr2[0][0] + arr1[1][0]
    if a > b :
        return (b)
    else:
        return (a)
else:
    return (arr1[0][0] + arr2[0][0])
