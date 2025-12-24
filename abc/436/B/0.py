N = int(input())
S = [[0] *  N for _ in range(N)]

y = 0
x = (N - 1) // 2
k = 1
S[y][x] = k
for _ in range(N * N - 1):
    ny = (y - 1) % N
    nx = (x + 1) % N
    if S[ny][nx] != 0:
        ny = (y + 1) % N
        nx = x
    k += 1
    S[ny][nx] = k
    y = ny
    x = nx

for line in S:
    print(*line)