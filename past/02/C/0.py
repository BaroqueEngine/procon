import sys
sys.setrecursionlimit(10**7)

N = int(input())
S = [list(input()) for _ in range(N)]


def dfs(x, y):
    if y == 0:
        return
    for dx in [-1, 0, 1]:
        tx = x + dx
        ty = y - 1
        if tx < 0 or tx >= 2 * N - 1:
            continue
        if S[ty][tx] != "#":
            continue
        S[ty][tx] = "X"
        dfs(tx, ty)


for y in range(N):
    for x in range(2 * N - 1):
        if S[y][x] == "X":
            dfs(x, y)

for line in S:
    print("".join(line))
