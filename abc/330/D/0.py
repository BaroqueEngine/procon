N = int(input())
S = [input() for _ in range(N)]

row = [0] * N
col = [0] * N

for y in range(N):
    for x in range(N):
        if S[y][x] == "o":
            row[y] += 1
            col[x] += 1

ans = 0
for y in range(N):
    for x in range(N):
        if S[y][x] == "x":
            continue
        ans += (col[x] - 1) * (row[y] - 1)

print(ans)
