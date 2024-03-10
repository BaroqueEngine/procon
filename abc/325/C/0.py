import sys
H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
seen = [[False] * W for _ in range(H)]
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

sys.setrecursionlimit(10**7)


def f(x, y):
    seen[y][x] = True
    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if S[ty][tx] == ".":
            continue
        if seen[ty][tx]:
            continue
        f(tx, ty)


for y in range(H):
    for x in range(W):
        if S[y][x] == "#" and not seen[y][x]:
            ans += 1
            f(x, y)
print(ans)
