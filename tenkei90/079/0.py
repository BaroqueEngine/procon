H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

cnt = 0
for y in range(H - 1):
    for x in range(W - 1):
        diff = B[y][x] - A[y][x]
        cnt += abs(diff)
        for ty in range(y, y + 2):
            for tx in range(x, x + 2):
                A[ty][tx] += diff

if A == B:
    print("Yes")
    print(cnt)
else:
    print("No")
