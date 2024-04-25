import heapq

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
INF = 10**18
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(sx, sy):
    hist = [[INF] * W for _ in range(H)]
    hist[sy][sx] = 0
    q = [(0, sx, sy)]
    while len(q) > 0:
        dist, x, y = heapq.heappop(q)
        if dist != hist[y][x]:
            continue
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            new_dist = dist + A[ty][tx]
            if new_dist < hist[ty][tx]:
                hist[ty][tx] = new_dist
                heapq.heappush(q, (new_dist, tx, ty))
    return hist


ans = INF
sx, sy = 0, H - 1
cx, cy = W - 1, H - 1
gx, gy = W - 1, 0
S = dijkstra(sx, sy)
C = dijkstra(cx, cy)
G = dijkstra(gx, gy)
for y in range(H):
    for x in range(W):
        ans = min(ans, S[y][x] + C[y][x] + G[y][x] - A[y][x] * 2)

print(ans)
