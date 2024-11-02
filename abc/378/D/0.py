import sys
sys.setrecursionlimit(10**7)

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0


def f(route, x, y):
    if len(route) == K + 1:
        return 1
    ret = 0
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if S[ty][tx] == "#":
            continue
        if (tx, ty) in route:
            continue
        new_route = route + [(tx, ty)]
        ret += f(new_route, tx, ty)
    return ret


for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            ans += f([(x, y)], x, y)
print(ans)
