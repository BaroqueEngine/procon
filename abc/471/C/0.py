N = int(input()) + 2
INF = 10**18
A = sorted([-INF] + list(map(int, input().split())) + [INF])

cur = 0
left = -INF
right = INF

for i in range(N):
    if A[i] < cur:
        left = max(left, i)
    if A[i] > cur:
        right = min(right, i)

ans = 0
for _ in range(N - 2):
    diff_l = abs(cur - A[left])
    diff_r = abs(cur - A[right])

    if diff_l <= diff_r:
        ans += diff_l
        cur = A[left]
        left -= 1
    else:
        ans += diff_r
        cur = A[right]
        right += 1

print(ans)