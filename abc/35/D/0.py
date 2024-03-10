import heapq

N, M, T = map(int, input().split())
money = list(map(int, input().split()))

G0 = [[] for _ in range(N)]
G1 = [[] for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    G0[A].append((B, C))
    G1[B].append((A, C))


def calc_dist(start, edge):
    q = [(0, start)]  # (time, index)
    dist = [10**18] * N
    dist[start] = 0

    while len(q) > 0:
        time, cur = heapq.heappop(q)
        if time > dist[cur]:
            continue

        for next, cost in edge[cur]:
            new_time = time + cost
            if new_time < dist[next]:
                dist[next] = new_time
                heapq.heappush(q, (new_time, next))

    return dist


d0 = calc_dist(0, G0)
d1 = calc_dist(0, G1)

ans = 0
for target in range(N):
    time = T
    time -= d0[target]
    time -= d1[target]

    if time < 0:
        time = 0

    ans = max(ans, time * money[target])

print(ans)
