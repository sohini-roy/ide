m = int(input().strip())
ar = [int(i) for i in input().strip().split()]

def partition(A, i):
    right = [];
    left = [];
    equal = [];
    x = len(A);
    if x >1:
        for j in range(0, x):
            if A[j]>A[i]:
                right.append(A[j]);
            else:
                if A[j]<A[i]:
                    left.append(A[j]);
                else:
                    equal.append(A[j]);
        left = partition(left, 0) + equal;
        left = left + partition(right, 0);
        return left;
    else:
        return A;

ar = partition(ar, 0);
print(ar);

#lomuto partition scheme:

# algorithm quicksort(A, lo, hi) is
#     if lo < hi then
#         p := partition(A, lo, hi)
#         quicksort(A, lo, p – 1)
#         quicksort(A, p + 1, hi)
#
# algorithm partition(A, lo, hi) is
#     pivot := A[hi]
#     i := lo - 1
#     for j := lo to hi - 1 do
#         if A[j] ≤ pivot then
#             i := i + 1
#             if i ≠ j then
#                 swap A[i] with A[j]
#     swap A[i+1] with A[hi]
#     return i + 1
