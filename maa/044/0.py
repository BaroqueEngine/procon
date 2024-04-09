import queue
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

dist = [-1] * N
dist[0] = 0

q = queue.Queue()
q.put(0)

while not q.empty():
    cur = q.get()
    for next in G[cur]:
        if dist[next] != -1:
            continue
        dist[next] = dist[cur] + 1
        q.put(next)

for x in dist:
    print(x)
