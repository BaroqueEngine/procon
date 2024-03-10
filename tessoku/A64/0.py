N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, C))
    G[B].append((A, C))

INF = 10**10
dist = [INF] * N

import heapq

heap = [(0, 0)]

dist[0] = 0

while len(heap) > 0:
    cur_dist, cur = heapq.heappop(heap)

    if cur_dist > dist[cur]:
        continue

    for next, cost in G[cur]:
        next_dist = dist[cur] + cost
        if next_dist < dist[next]:
            dist[next] = next_dist
            heapq.heappush(heap, (next_dist, next))

for i in range(N):
    if dist[i] == INF:
        dist[i] = -1
    print(dist[i])
