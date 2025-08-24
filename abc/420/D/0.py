import queue
H, W = map(int, input().split())
A = [input() for _ in range(H)]
sx, sy, gx, gy = -1, -1, -1, -1
for y in range(H):
    for x in range(W):
        if A[y][x] == "S":
            sx = x
            sy = y
        elif A[y][x] == "G":
            gx = x
            gy = y

INF = 10**18
dist_table = [[[INF] * W for _ in range(H)] for _ in range(2)]
dist_table[0][sy][sx] = 0

q = queue.Queue()
q.put((sx, sy, 0, 0))

door = {
    "o": 0,
    "x": 1
}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while not q.empty():
    x, y, toggle, dist = q.get()
    
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        new_toggle = toggle
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if A[ty][tx] == "#":
            continue
        if A[ty][tx] in "ox" and door[A[ty][tx]] != toggle:
            continue
        if A[ty][tx] == "?":
            new_toggle = (toggle + 1) % 2
        if dist + 1 >= dist_table[new_toggle][ty][tx]:
            continue
        dist_table[new_toggle][ty][tx] = dist + 1
        q.put((tx, ty, new_toggle, dist + 1))

ans = min(dist_table[0][gy][gx], dist_table[1][gy][gx])
if ans == INF:
    ans = -1
print(ans)