import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    U, V, B = map(int, input().split())
    U -= 1
    V -= 1
    G[U].append((V, B))
    G[V].append((U, B))

hist = [10**18] * N
hist[0] = A[0]
q = [(A[0], 0)]

while len(q) > 0:
    total_cost, cur = heapq.heappop(q)
    if hist[cur] != total_cost:
        continue
    for next, cost in G[cur]:
        new_cost = total_cost + cost + A[next]
        if new_cost < hist[next]:
            hist[next] = new_cost
            heapq.heappush(q, (new_cost, next))

print(*hist[1:])
