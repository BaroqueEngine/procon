N = int(input())
SIZE = 2000
S = [[0] * (SIZE + 1) for _ in range(SIZE + 1)]
G = []

for _ in range(N):
    y1, y2, x1, x2 = map(int, input().split())
    y1 -= 1
    y2 -= 1
    x1 -= 1
    x2 -= 1
    S[y1][x1] += 1
    S[y1][x2 + 1] -= 1
    S[y2 + 1][x1] -= 1
    S[y2 + 1][x2 + 1] += 1
    G.append((x1, y1, x2, y2))

for y in range(SIZE + 1):
    for x in range(SIZE):
        S[y][x + 1] += S[y][x]

for x in range(SIZE + 1):
    for y in range(SIZE):
        S[y + 1][x] += S[y][x]

T = [[0] * (SIZE + 1) for _ in range(SIZE + 1)]

zero_num = 0
for y in range(SIZE):
    for x in range(SIZE):
        zero_num += 1 if S[y][x] == 0 else 0
        is_one = 1 if S[y][x] == 1 else 0
        T[y + 1][x + 1] = T[y][x + 1] + T[y + 1][x] - T[y][x] + is_one

ans = []
for x1, y1, x2, y2 in G:
    ans.append(T[y2 + 1][x2 + 1] - T[y1][x2 + 1] - T[y2 + 1][x1] + T[y1][x1] + zero_num)

for x in ans:
    print(x)