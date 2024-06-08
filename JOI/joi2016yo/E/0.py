import queue
import heapq
N, M, K, S = map(int, input().split())
price = list(map(int, input().split()))
danger = [False] * N
warning = [False] * N
for _ in range(K):
    danger[int(input()) - 1] = True
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

seen = [False] * N
q = queue.Queue()
for i in range(N):
    if danger[i]:
        seen[i] = True
        q.put((i, 0))

while not q.empty():
    cur, dist = q.get()
    if dist == S:
        continue
    for next in G[cur]:
        if seen[next]:
            continue
        seen[next] = True
        warning[next] = True
        q.put((next, dist + 1))

INF = 10**18
hist = [INF] * N
hist[0] = 0
q = [(0, 0)]
while len(q) > 0:
    dist, cur = heapq.heappop(q)
    if dist != hist[cur]:
        continue
    for next in G[cur]:
        if danger[next]:
            continue
        cost = 0
        if next not in [0, N - 1]:
            cost = price[1 if warning[next] else 0]
        new_cost = dist + cost
        if new_cost < hist[next]:
            hist[next] = new_cost
            heapq.heappush(q, (new_cost, next))
print(hist[N - 1])
