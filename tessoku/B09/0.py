SIZE = 1510
S = [[0] * SIZE for _ in range(SIZE)]
N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    S[y1][x1] += 1
    S[y2][x2] += 1
    S[y1][x2] -= 1
    S[y2][x1] -= 1

for y in range(SIZE):
    for x in range(SIZE - 1):
        S[y][x + 1] += S[y][x]

for x in range(SIZE):
    for y in range(SIZE - 1):
        S[y + 1][x] += S[y][x]

ans = 0
for y in range(SIZE):
    for x in range(SIZE):
        if S[y][x] >= 1:
            ans += 1
print(ans)
