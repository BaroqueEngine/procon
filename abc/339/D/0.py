import queue
N = int(input())
M = [input() for _ in range(N)]

start = []
for y in range(N):
    for x in range(N):
        if M[y][x] == "P":
            start.append((x, y))

dist = [[[[0 for a in range(N)] for b in range(N)]
         for c in range(N)] for d in range(N)]
for y0 in range(N):
    for x0 in range(N):
        for y1 in range(N):
            for x1 in range(N):
                dist[x0][y0][x1][y1] = -1

dist[start[0][0]][start[0][1]][start[1][0]][start[1][1]] = 0
q = queue.Queue()
a, b = start[0]
c, d = start[1]
q.put((a, b, c, d))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, dir_x, dir_y):
    x += dir_x
    y += dir_y

    if x < 0 or x >= N or y < 0 or y >= N or (M[y][x] == "#"):
        return (x - dir_x, y - dir_y)
    return (x, y)


while not q.empty():
    a, b, c, d = q.get()

    for i in range(4):
        e, f = move(a, b, dx[i], dy[i])
        g, h = move(c, d, dx[i], dy[i])

        if (e, f) == (g, h):
            print(dist[a][b][c][d] + 1)
            exit()

        if (a, b, c, d) == (e, f, g, h):
            continue

        if dist[e][f][g][h] != -1:
            continue
        dist[e][f][g][h] = dist[a][b][c][d] + 1

        q.put((e, f, g, h))

print(-1)
