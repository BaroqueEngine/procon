from collections import deque
H, W = map(int, input().split())
M = [input() for _ in range(H)]
INF = 10**18
sx, sy = None, None
gx, gy = None, None

for y in range(H):
    for x in range(W):
        if M[y][x] == "S":
            sx, sy = x, y
        if M[y][x] == "G":
            gx, gy = x, y

dir = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]]
ans = INF
for i in range(2):
    A = [[INF] * W for _ in range(H)]
    A[sy][sx] = 0
    q = deque([])
    q.append((sx, sy, 0, i))

    while len(q):
        x, y, step, prev_move_x = q.popleft()
        for dx, dy in dir[prev_move_x]:
            tx = x + dx
            ty = y + dy
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if M[ty][tx] == "#":
                continue
            if A[ty][tx] <= step + 1:
                continue
            A[ty][tx] = step + 1
            q.append((tx, ty, step + 1, not prev_move_x))
    ans = min(ans, A[gy][gx])

if ans == INF:
    ans = -1
print(ans)
