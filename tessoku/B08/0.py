N = int(input())
SIZE = 1510
M = [[0] * (SIZE) for _ in range(SIZE)]
for _ in range(N):
    X, Y = map(int, input().split())
    M[Y][X] += 1

for y in range(SIZE):
    for x in range(SIZE-1):
        M[y][x + 1] += M[y][x]

for x in range(SIZE):
    for y in range(SIZE-1):
        M[y + 1][x] += M[y][x]

Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    print(M[y2 + 1][x2 + 1] - M[y1][x2 + 1] - M[y2 + 1][x1] + M[y1][x1])
