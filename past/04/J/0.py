import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N + 6)]
X = list(map(int, input().split()))
S = input()
AIN = N
AOUT = AIN + 1
BIN = AOUT + 1
BOUT = BIN + 1
CIN = BOUT + 1
COUT = CIN + 1
G[AIN].append((BOUT, X[0]))
G[AIN].append((COUT, X[1]))
G[BIN].append((AOUT, X[0]))
G[BIN].append((COUT, X[2]))
G[CIN].append((AOUT, X[1]))
G[CIN].append((BOUT, X[2]))

for i in range(N):
    if S[i] == "A":
        G[i].append((AIN, 0))
        G[AOUT].append((i, 0))
    if S[i] == "B":
        G[i].append((BIN, 0))
        G[BOUT].append((i, 0))
    if S[i] == "C":
        G[i].append((CIN, 0))
        G[COUT].append((i, 0))

for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, C))
    G[B].append((A, C))

hist = [10**18] * (N + 6)
hist[0] = 0

q = [(0, 0)]
while len(q) > 0:
    dist, cur = heapq.heappop(q)
    if dist != hist[cur]:
        continue
    for next, cost in G[cur]:
        new_cost = dist + cost
        if new_cost < hist[next]:
            hist[next] = new_cost
            heapq.heappush(q, (new_cost, next))
print(hist[N - 1])
