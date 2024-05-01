import queue
N, M, K = map(int, input().split())
H = list(map(int, input().split()))
C = [x - 1 for x in list(map(int, input().split()))]
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if H[A] < H[B]:
        G[A].append(B)
    else:
        G[B].append(A)

INF = 10**18
dist = [INF] * N
q = queue.Queue()
for c in C:
    dist[c] = 0
    q.put(c)

while not q.empty():
    cur = q.get()
    for next in G[cur]:
        if dist[next] != INF:
            continue
        dist[next] = dist[cur] + 1
        q.put(next)

for x in dist:
    if x == INF:
        print(-1)
    else:
        print(x)
