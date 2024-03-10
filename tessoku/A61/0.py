N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

for i in range(N):
    f = "{}: {}".format(i + 1, [x + 1 for x in G[i]])
    f = f.replace("[", "{")
    f = f.replace("]", "}")
    print(f)
