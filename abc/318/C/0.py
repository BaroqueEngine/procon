N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)

ans = 0
for i in range(0, N, D):
    total = sum(F[i : i + D])
    ans += min(total, P)
print(ans)
