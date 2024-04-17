H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

row = []
for line in A:
    row.append(sum(line))
col = []
for line in zip(*A):
    col.append(sum(line))

for y in range(H):
    line = []
    for x in range(W):
        line.append(row[y] + col[x] - A[y][x])
    print(*line)