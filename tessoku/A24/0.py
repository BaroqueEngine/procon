import bisect

N = int(input())
A = list(map(int, input().split()))

arr = [A[0]]

for x in A:
    if arr[-1] < x:
        arr.append(x)
    else:
        pos = bisect.bisect_left(arr, x)
        arr[pos] = x

print(len(arr))
