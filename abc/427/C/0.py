N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

ans = 10**18
for bit in range(2 ** N):
    cnt = 0
    for u, v in edges:
        if (bit >> u) & 1 == (bit >> v) & 1:
            cnt += 1
    ans = min(ans, cnt)

print(ans)