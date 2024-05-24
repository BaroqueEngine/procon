H, W, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
C = [None] + list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for y in range(H):
    for x in range(W):
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if A[y][x] == A[ty][tx]:
                continue
            if C[A[y][x]] == C[A[ty][tx]]:
                print("No")
                exit()
print("Yes")
