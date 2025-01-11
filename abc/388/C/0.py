import bisect

N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(N - 1):
    base = A[i]
    target = base * 2
    pos = bisect.bisect_left(A, target)
    ans += N - pos

print(ans)
