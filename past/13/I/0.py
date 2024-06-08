import queue
N, M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[B].append(A)
    deg[A] += 1

q = queue.Queue()
for i in range(N):
    if deg[i] == 0:
        q.put(i)

while not q.empty():
    cur = q.get()
    for next in G[cur]:
        deg[next] -= 1
        if deg[next] == 0:
            q.put(next)

print("Yes" if sum(deg) == 0 else "No")
