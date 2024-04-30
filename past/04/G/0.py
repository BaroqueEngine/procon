H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

def f(sx, sy):
    S[sy][sx] = "."
    seen = [[False] * W for _ in range(H)]
    stack = [(sx, sy)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while len(stack) > 0:
        x, y = stack.pop()
        seen[y][x] = True
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if S[ty][tx] == "#":
                continue
            if seen[ty][tx]:
                continue
            stack.append((tx, ty))
    ok = True
    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                continue
            if not seen[y][x]:
                ok = False
    S[sy][sx] = "#"
    return ok

ans = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            ans += f(x, y)
print(ans)