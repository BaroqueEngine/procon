N, W = map(int, input().split())
pos = [[] for _ in range(W)]
vanished = [10**18] * N
for i in range(N):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    pos[X].append((Y, i))

min_cnt = 10**18
for p in pos:
    p.sort()
    min_cnt = min(min_cnt, len(p))

time = 0
for i in range(min_cnt):
    max_y = 0
    for x in range(W):
        max_y = max(max_y, pos[x][i][0] - time)
    for x in range(W):
        vanished[pos[x][i][1]] = time + max_y + 1
    time += max_y

ans = []
Q = int(input())
for _ in range(Q):
    T, A = map(int, input().split())
    A -= 1
    ans.append("Yes" if T < vanished[A] else "No")

for x in ans:
    print(x)
