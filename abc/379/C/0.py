N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))
G = sorted(zip(X, A))
G.append((N + 1, 0))  # 番兵
if G[0][0] != 1 or sum(A) != N:
    print(-1)
    exit()

move_count = 0
stones = 0
for i in range(M):
    stones += G[i][1]
    dist = G[i + 1][0] - G[i][0]
    u = stones - 1
    v = stones - dist
    move_count += (u + v) * dist // 2
    stones -= dist
    if stones < 0:
        print(-1)
        exit()

print(move_count)
