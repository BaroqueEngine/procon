N, M = map(int, input().split())

cnt = [-1] * M
for _ in range(N):
    C, S = map(int, input().split())
    C -= 1
    cnt[C] = max(cnt[C], S)

print(*[x for x in cnt])
    