N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

for g in G:
    g.sort()

for i in range(1, N + 1):
    line = ", ".join(map(str, G[i]))
    print("{0}: {{{1}}}".format(i, line))