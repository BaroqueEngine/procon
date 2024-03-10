N = int(input())
M = [[0 for _ in range(N)] for _ in range(N)]

M[N // 2][N // 2] = "T"

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir = 0

x, y = 0, 0
num = 1

while M[y][x] != "T":
    M[y][x] = num
    num += 1
    tx = x + dx[dir]
    ty = y + dy[dir]
    if tx < 0 or tx >= N or ty < 0 or ty >= N or M[ty][tx] != 0:
        dir = (dir + 1) % 4
        tx = x + dx[dir]
        ty = y + dy[dir]
    x = tx
    y = ty

for line in M:
    print(*line)
