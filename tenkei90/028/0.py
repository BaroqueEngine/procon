N = int(input())
LEN = 1010
S = [[0] * LEN for _ in range(LEN)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x2 -= 1
    y2 -= 1
    S[y1][x1] += 1
    S[y2 + 1][x2 + 1] += 1
    S[y1][x2 + 1] -= 1
    S[y2 + 1][x1] -= 1

for y in range(LEN):
    for x in range(LEN-1):
        S[y][x + 1] += S[y][x]

for x in range(LEN):
    for y in range(LEN-1):
        S[y + 1][x] += S[y][x]

dic = {}
for i in range(N + 1):
    dic[i] = 0

for y in range(LEN):
    for x in range(LEN):
        dic[S[y][x]] += 1

for i in range(1, N + 1):
    print(dic[i])
