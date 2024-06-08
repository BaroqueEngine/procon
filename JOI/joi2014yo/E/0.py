from heapq import heappush, heappop
from collections import deque

INF = 10**18
N, K = map(int, input().split())
cost = []
step = []
for _ in range(N):
    X, Y = map(int, input().split())
    cost.append(X)
    step.append(Y)
G = [[] for _ in range(N)]
for _ in range(K):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

G2 = [[] for _ in range(N)]

for start in range(N):
    q = deque([start])
    hist = [INF] * N
    hist[start] = 0
    while len(q) > 0:
        cur = q.popleft()
        if hist[cur] == step[start]:
            continue
        for next in G[cur]:
            if hist[next] != INF:
                continue
            hist[next] = hist[cur] + 1
            G2[start].append(next)
            q.append(next)

hist = [INF] * N
hist[0] = 0
q = [(0, 0)]
while len(q) > 0:
    dist, cur = heappop(q)
    if hist[cur] != dist:
        continue
    for next in G2[cur]:
        if dist + cost[cur] < hist[next]:
            hist[next] = dist + cost[cur]
            heappush(q, (hist[next], next))
print(hist[-1])
