N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    best_dist = 0
    best_index = None
    for j in range(N):
        if i == j:
            continue
        dx = A[i][0] - A[j][0]
        dy = A[i][1] - A[j][1]
        dist = dx * dx + dy * dy
        if dist > best_dist:
            best_index = j + 1
            best_dist = dist
    print(best_index)
