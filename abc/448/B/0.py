N, M = map(int, input().split())
C = list(map(int, input().split()))

ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    A -= 1
    cnt = min(B, C[A])
    C[A] -= cnt
    ans += cnt

print(ans)