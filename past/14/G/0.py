H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for y in range(H):
    for x in range(W):
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if A[y][x] < A[ty][tx]:
                ans.append((A[y][x], A[ty][tx]))
ans.sort()
for a, b in ans:
    print("{} {}".format(a, b))
