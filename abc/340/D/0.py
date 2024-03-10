import heapq

N = int(input())
G = [[] for _ in range(N + 1)]
for i in range(1, N):
    A, B, X = map(int, input().split())
    G[i].append((i + 1, A))
    G[i].append((X, B))

dist = [10**18] * (N + 1)
dist[1] = 0

q = [(0, 1)]  # (dist, index)

while len(q) > 0:
    cur_dist, cur = heapq.heappop(q)
    if cur_dist > dist[cur]:
        continue

    for next, cost in G[cur]:
        new_dist = cur_dist + cost
        if new_dist < dist[next]:
            dist[next] = new_dist
            heapq.heappush(q, (new_dist, next))

print(dist[N])
