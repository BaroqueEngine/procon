H, W = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(H)]

def shoot(x, y):
    if S[y][x] == 0:
        return
    S[y][x] = 0
    for ty in range(y - 1, -1, -1):
        S[ty + 1][x] = S[ty][x]
    S[0][x] = 0

N = int(input())
for _ in range(N):
    Y, X = map(int, input().split())
    X -= 1
    Y -= 1
    shoot(X, Y)

for line in S:
    print(*line)