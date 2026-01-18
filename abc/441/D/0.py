import sys
sys.setrecursionlimit(10**7)

N, M, L, S, T = map(int, input().split())
G = [[] for _ in range(N)]
ok = [False] * N

for _ in range(M):
    U, V, C = map(int, input().split())
    U -= 1
    V -= 1
    G[U].append((V, C))

def f(i, cur, cost):
    if i == L:
        if S <= cost <= T:
            ok[cur] = True
        return

    for next, next_cost in G[cur]:
        f(i + 1, next, cost + next_cost)

f(0, 0, 0)

ans = []
for i in range(N):
    if ok[i]:
        ans.append(i + 1)

print(*ans)