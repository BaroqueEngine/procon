N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

ans = 0
for i in range(N):
    cnt = 0
    for x in G[i]:
        if x < i:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)
