from collections import deque
import string

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

INF = 10**18
dist = [[INF] * W for _ in range(H)]
dist[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([(0, 0)])

warp = {}
use_warp = {}
for c in string.ascii_letters:
    warp[c] = []
    use_warp[c] = False

for y in range(H):
    for x in range(W):
        if "a" <= S[y][x] <= "z":
            warp[S[y][x]].append((x, y))

while len(q) > 0:
    x, y = q.popleft()
    for i in range(len(dx)):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        tc = S[ty][tx]
        if tc == "#":
            continue
        if dist[ty][tx] == INF:
            dist[ty][tx] = dist[y][x] + 1
            q.append((tx, ty))
    if "a" <= S[y][x] <= "z":
        if use_warp[S[y][x]]:
            continue
        use_warp[S[y][x]] = True
        for tx, ty in warp[S[y][x]]:
            if x == tx and y == ty:
                continue
            if dist[ty][tx] == INF:
                dist[ty][tx] = dist[y][x] + 1
                q.append((tx, ty))

if dist[-1][-1] == INF:
    dist[-1][-1] = -1

print(dist[-1][-1])
