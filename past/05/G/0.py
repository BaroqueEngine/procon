import sys
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
M = [input() for _ in range(H)]
snake_len = 0
for y in range(H):
    for x in range(W):
        if M[y][x] == "#":
            snake_len += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def f(x, y, route, seen):
    seen[y][x] = True
    if len(route) == snake_len:
        print(snake_len)
        for x, y in route:
            print(y + 1, x + 1)
        exit()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if M[ty][tx] == ".":
            continue
        if seen[ty][tx]:
            continue
        f(tx, ty, route + [(tx, ty)], seen)
    seen[y][x] = False

for y in range(H):
    for x in range(W):
        if M[y][x] == "#":
            f(x, y, [(x, y)], [[False] * W for _ in range(H)])