import heapq
H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
N = int(input())
med = [[0] * W for _ in range(H)]

for _ in range(N):
    Y, X, E = map(int, input().split())
    Y -= 1
    X -= 1
    med[Y][X] = E

dist = [[-1] * W for _ in range(H)]
q = []
for y in range(H):
    for x in range(W):
        if A[y][x] == "S":
            e = med[y][x]
            dist[y][x] = e
            q.append((-e, x, y))
            med[y][x] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while len(q) > 0:
    e, x, y = heapq.heappop(q)
    e = -e

    if A[y][x] == "T":
        print("Yes")
        exit()

    if e < dist[y][x]:
        continue

    if e == 0:
        continue
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if A[ty][tx] == "#":
            continue
        next_e = max(e - 1, med[ty][tx])
        if next_e != e - 1:
            med[ty][tx] = 0
        if next_e <= dist[ty][tx]:
            continue
        dist[ty][tx] = next_e
        heapq.heappush(q, (-next_e, tx, ty))

print("No")
