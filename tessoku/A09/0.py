H, W, N = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(N)]
S = [[0] * (W + 1) for _ in range(H + 1)]

for y0, x0, y1, x1 in M:
    x0 -= 1
    y0 -= 1
    x1 -= 1
    y1 -= 1

    S[y0][x0] += 1
    S[y1 + 1][x1 + 1] += 1
    S[y0][x1 + 1] -= 1
    S[y1 + 1][x0] -= 1

for y in range(H):
    for x in range(W):
        S[y][x + 1] += S[y][x]

for x in range(W):
    for y in range(H):
        S[y + 1][x] += S[y][x]

for y in range(H):
    print(*S[y][:W])
