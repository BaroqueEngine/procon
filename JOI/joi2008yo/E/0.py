import heapq
N, M = map(int, input().split())
G = [[] for _ in range(N)]


def dijkstra(start, end):
    INF = 10**18
    hist = [INF] * N
    hist[start] = 0
    q = [(0, start)]
    while len(q) > 0:
        dist, cur = heapq.heappop(q)
        if dist != hist[cur]:
            continue
        for next, cost in G[cur]:
            new_cost = dist + cost
            if new_cost < hist[next]:
                hist[next] = new_cost
                heapq.heappush(q, (new_cost, next))

    if hist[end] == INF:
        hist[end] = -1
    return hist[end]


ans = []
for _ in range(M):
    Q = list(map(int, input().split()))
    if Q[0] == 0:
        u, v = Q[1:]
        u -= 1
        v -= 1
        ans.append(dijkstra(u, v))
    else:
        u, v, cost = Q[1:]
        u -= 1
        v -= 1
        G[u].append((v, cost))
        G[v].append((u, cost))

for x in ans:
    print(x)
