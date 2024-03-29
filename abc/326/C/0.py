import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


ans = 0

for i in range(N):
    right = bisect.bisect_left(A, A[i] + M)
    ans = max(ans, right - i)

print(ans)
