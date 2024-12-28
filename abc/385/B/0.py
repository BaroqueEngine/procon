H, W, y, x = map(int, input().split())
y -= 1
x -= 1
M = [list(input()) for _ in range(H)]
D = input()

dir = "LRUD"
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

for d in D:
    i = dir.index(d)
    x += dx[i]
    y += dy[i]

    if M[y][x] == "#":
        x -= dx[i]
        y -= dy[i]

    if M[y][x] == "@":
        M[y][x] = "."
        ans += 1

print(y + 1, x + 1, ans)
