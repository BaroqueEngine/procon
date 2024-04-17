import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, C))
    G[B].append((A, C))


def dijkstra(start):
    q = [(0, start)]
    score = [10**18] * N
    score[start] = 0
    while len(q) > 0:
        dist, cur = heapq.heappop(q)
        if dist != score[cur]:
            continue
        for next, cost in G[cur]:
            new_dist = dist + cost
            if new_dist < score[next]:
                score[next] = new_dist
                heapq.heappush(q, (new_dist, next))
    return score


start_dist = dijkstra(0)
end_dist = dijkstra(N - 1)
for i in range(N):
    print(start_dist[i] + end_dist[i])
