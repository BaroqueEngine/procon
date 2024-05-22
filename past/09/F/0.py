import sys
sys.setrecursionlimit(10**7)

sy, sx = map(int, input().split())
sx -= 1
sy -= 1
S = [input() for _ in range(3)]

dir = []
for y in range(3):
    for x in range(3):
        if S[y][x] == "#":
            dir.append((x - 1, y - 1))

N = 9
seen = [[False] * N for _ in range(N)]

def dfs(x, y):
    seen[y][x] = True

    for dx, dy in dir:
        tx = x + dx
        ty = y + dy
        if tx < 0 or tx >= N or ty < 0 or ty >= N:
            continue
        if seen[ty][tx]:
            continue
        dfs(tx, ty)

dfs(sx, sy)

ans = 0
for y in range(N):
    ans += sum(seen[y])
print(ans)