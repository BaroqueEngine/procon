N, Q = map(int, input().split())
total_y = [0] * N # 縦ごとに現在何個積まれているか
total_x = [0] * (3 * (10**6)) # 横ごとに現在何個積まれているか
delete_lines = 0
ans = []

for _ in range(Q):
    op, x = map(int, input().split())
    if op == 1:
        x -= 1
        total_y[x] += 1
        total_x[total_y[x] - 1] += 1
        if total_x[total_y[x] - 1] == N:
            delete_lines += 1
    else:
        y = max(0, x + delete_lines)
        ans.append(total_x[y - 1])

for x in ans:
    print(x)