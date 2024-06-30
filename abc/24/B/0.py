N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
next_close_time = 0

for i in range(N):
    if next_close_time <= A[i]:
        ans += T
    else:
        ans += A[i] - A[i - 1]
    next_close_time = A[i] + T
print(ans)
