# n = int(input().strip())
# a = []
# for a_i in range(n):
    # a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    # a.append(a_t)
# print(a);
# print(a[2][2]);

#printing lower matrix

# n = int(input().strip())
# for i in range(0, n):
#     for j in range(0, n):
#         if i >= j :
#             print('#');
#         else:
#             print(' ');
#
#blowing longest candles

# n = int(input());
#
# sums = 0;
# large = 0;
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')];
# for i in range (0, n):
#     if arr[i] > large :
#         large = arr[i];
#         sums = 1;
#     else:
#         if(large == arr[i]):
#             sums += 1;
#
# print(sums, large);
