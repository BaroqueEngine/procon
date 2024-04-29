N, M, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    G[U].append(V)
    G[V].append(U)
C = list(map(int, input().split()))
ans = []
for _ in range(Q):
    S = list(map(int, input().split()))
    if S[0] == 1:
        x = S[1]
        x -= 1
        ans.append(C[x])
        for y in G[x]:
            C[y] = C[x]
    else:
        x, y = S[1:]
        x -= 1
        ans.append(C[x])
        C[x] = y

for x in ans:
    print(x)
