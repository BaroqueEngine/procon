import sys
sys.setrecursionlimit(10**7)
N, M = map(int, input().split())

uv = [[] for _ in range(N + 1)]
vu = [[] for _ in range(N + 1)]

for _ in range(M):
    U, V, W = map(int, input().split())
    uv[U].append((V, W))
    vu[V].append((U, W))

ans = [None] * (N + 1)


def dfs(cur):
    for v, w in uv[cur]:
        if ans[v] != None:
            continue
        ans[v] = ans[cur] + w
        dfs(v)

    for u, w in vu[cur]:
        if ans[u] != None:
            continue
        ans[u] = ans[cur] - w
        dfs(u)


for i in range(1, N + 1):
    if ans[i] != None:
        continue
    ans[i] = 0
    dfs(i)

print(*ans[1:])
