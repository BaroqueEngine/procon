import heapq

N, M, Y = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    U, V, T = map(int, input().split())
    U -= 1
    V -= 1
    G[U].append((V, T))
    G[V].append((U, T))

X = list(map(int, input().split()))
for i in range(N):
    G[i].append((N, X[i] + Y))
    G[N].append((i, X[i]))

hist = [10**18] * (N + 1)
hist[0] = 0

q = [(0, 0)] # 総距離, i
while len(q) > 0:
    dist, cur = heapq.heappop(q)
    if hist[cur] != dist:
        continue
    for nxt, cost in G[cur]:
        new_dist = dist + cost
        if hist[nxt] <= new_dist:
            continue
        hist[nxt] = new_dist
        heapq.heappush(q, (new_dist, nxt))

print(*hist[1:N])