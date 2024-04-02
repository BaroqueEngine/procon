N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, C))
    G[B].append((A, C))

INF = 10**18
dist = [INF] * N
dist[0] = 0

prev = [None] * N

import heapq
q = [(0, 0)] # (cost, index)

while len(q) > 0:
    cost, cur = heapq.heappop(q)
    if dist[cur] != cost:
        continue

    for next, next_cost in G[cur]:
        new_cost = cost + next_cost
        if new_cost < dist[next]:
            dist[next] = new_cost
            heapq.heappush(q, (new_cost, next))
            prev[next] = cur

route = []
cur = N - 1
while cur != None:
    route.append(cur + 1)
    cur = prev[cur]

print(*route[::-1])