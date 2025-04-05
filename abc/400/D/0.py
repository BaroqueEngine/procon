from collections import deque

H, W = map(int, input().split())
S = [input().strip() for _ in range(H)]

sy, sx, gy, gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1

INF = 10**18
dist = [[INF] * W for _ in range(H)]
dist[sy][sx] = 0

q = deque([])
q.append((0, sx, sy)) 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while len(q) > 0:
    k, x, y = q.popleft()

    if k > dist[y][x]:
        continue

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < W and 0 <= ty < H:
            if S[ty][tx] == ".":
                if k < dist[ty][tx]:
                    dist[ty][tx] = k
                    q.appendleft((k, tx, ty))

    for i in range(4):
        for j in [1, 2]:
            tx = x + dx[i] * j
            ty = y + dy[i] * j
            if 0 <= tx < W and 0 <= ty < H:
                if k + 1 < dist[ty][tx]:
                    dist[ty][tx] = k + 1
                    q.append((k + 1, tx, ty))

ans = dist[gy][gx]
if ans == INF:
    ans = -1
print(ans)
