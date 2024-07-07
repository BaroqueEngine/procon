from collections import deque
N, K = map(int, input().split())
M = N - K
A = list(map(int, input().split()))
A.sort()

arr = deque(A[:M])
min_v = arr[-1] - arr[0]
for i in range(M, N):
    arr.popleft()
    arr.append(A[i])
    min_v = min(min_v, arr[-1] - arr[0])
print(min_v)
