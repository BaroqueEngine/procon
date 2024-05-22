import heapq
N, M = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(M)]
G = {}

seen = set([1, N])
for a, b, c in P:
    if a not in G:
        G[a] = set()
    if b not in G:
        G[b] = set()
    G[a].add((b, c))
    G[b].add((a, c))
    seen.add(a)
    seen.add(b)

seen = list(seen)
seen.sort()

for i in range(len(seen) - 1):
    u, v = seen[i], seen[i + 1]
    cost = v - u
    if u not in G:
        G[u] = set()
    if v not in G:
        G[v] = set()
    G[u].add((v, cost))
    G[v].add((u, cost))

q = [(0, 1)] # dist, floor
hist = {}
for x in seen:
    hist[x] = 10**18
hist[1] = 0

while len(q) > 0:
    dist, cur = heapq.heappop(q)
    if dist != hist[cur]:
        continue
    for next, cost in G[cur]:
        new_cost = dist + cost
        if new_cost < hist[next]:
            hist[next] = new_cost
            heapq.heappush(q, (new_cost, next))

print(hist[N])
