import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for i in range(M):
    A, B, C = map(int, input().split())
    G[A].append((B, C, i + 1))
    G[B].append((A, C, i + 1))

dist = [10**18] * (N + 1)
dist[1] = 0

q = [(0, 1)]  # (dist, index)
ans_temp = [-1] * (N + 1)

while len(q) > 0:
    cur_dist, cur = heapq.heappop(q)
    if cur_dist > dist[cur]:
        continue
    for next, cost, edge_index in G[cur]:
        next_dist = cur_dist + cost
        if next_dist < dist[next]:
            dist[next] = next_dist
            ans_temp[next] = edge_index
            heapq.heappush(q, (next_dist, next))

ans = []
for x in ans_temp:
    if x != -1:
        ans.append(x)

print(*ans)
