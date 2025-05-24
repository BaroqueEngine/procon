import sys
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

blocked = [[False] * W for _ in range((H))]

def calc_score():
    global ans
    score = 0
    for y in range(H):
        for x in range(W):
            if not blocked[y][x]:
                score ^= A[y][x]
    return score

def f(x, y):
    if x >= W:
        x = 0
        y += 1
    if y >= H:
        return calc_score()

    score = 0
    if x + 1 < W and not blocked[y][x] and not blocked[y][x + 1]:
        blocked[y][x] = True
        blocked[y][x + 1] = True
        score = max(score, f(x + 2, y))
        blocked[y][x] = False
        blocked[y][x + 1] = False
    if y + 1 < H and not blocked[y][x] and not blocked[y + 1][x]:
        blocked[y][x] = True
        blocked[y + 1][x] = True
        score = max(score, f(x + 1, y))
        blocked[y][x] = False
        blocked[y + 1][x] = False
    return max(score, f(x + 1, y))

print(f(0, 0))