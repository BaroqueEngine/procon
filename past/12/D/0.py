N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    U, V = map(int, input().split())

    if U == V:
        print("No")
        exit()

    if not(1 <= U <= N):
        print("No")
        exit()
    if not(1 <= V <= N):
        print("No")
        exit()
    
    if V in G[U]:
        print("No")
        exit()
    if U in G[V]:
        print("No")
        exit()
    G[U].append(V)
    G[V].append(U)

print("Yes")