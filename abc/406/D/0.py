H, W, N = map(int, input().split())
R = [set([]) for _ in range(H)]
C = [set([]) for _ in range(W)]

for _ in range(N):
    Y, X = map(int, input().split())
    X -= 1
    Y -= 1
    R[Y].add(X)
    C[X].add(Y)

ans = []
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        y = query[1] - 1
        ans.append(len(R[y]))
        for x in R[y]:
            C[x].remove(y)
        R[y] = set([])
    else:
        x = query[1] - 1
        ans.append(len(C[x]))
        for y in C[x]:
            R[y].remove(x)
        C[x] = set([])

for x in ans:
    print(x)