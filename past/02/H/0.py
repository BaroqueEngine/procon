H, W = map(int, input().split())
A = [input() for _ in range(H)]
pos = [[] for _ in range(11)]
for y in range(H):
    for x in range(W):
        if A[y][x] == "S":
            pos[0].append((x, y))
        elif A[y][x] == "G":
            pos[10].append((x, y))
        else:
            pos[int(A[y][x])].append((x, y))

ok = True
for i in range(1, 10):
    if len(pos[i]) == 0:
        ok = False
if not ok:
    print(-1)
    exit()

INF = 10**18
dp = [[[INF] * W for _ in range(H)] for __ in range(11)]
dp[0][pos[0][0][1]][pos[0][0][0]] = 0
for i in range(1, 11):
    for prev_x, prev_y in pos[i - 1]:
        for cur_x, cur_y in pos[i]:
            dist = abs(cur_x - prev_x) + abs(cur_y - prev_y)
            dp[i][cur_y][cur_x] = min(
                dp[i][cur_y][cur_x], dp[i - 1][prev_y][prev_x] + dist)

if dp[-1][pos[-1][0][1]][pos[-1][0][0]] == INF:
    dp[-1][pos[-1][0][1]][pos[-1][0][0]] = -1
print(dp[-1][pos[-1][0][1]][pos[-1][0][0]])
