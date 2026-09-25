from collections import defaultdict

N, Q = map(int, input().split())
S = 400000 # 番兵基準
NONE = -1

up = defaultdict(int)
down = defaultdict(int)

for i in range(1, N + 1):
    up[S + i] = i
    down[i] = S + i
    up[i] = NONE

for _ in range(Q):
    C, P = map(int, input().split())
    prev_p = down[C]
    down[C] = P
    up[P] = C
    if prev_p != NONE:
        up[prev_p] = NONE

ans = []
for i in range(1, N + 1):
    cnt = 0
    cur = S + i
    while up[cur] != NONE:
        cur = up[cur]
        cnt += 1
    ans.append(cnt)

print(*ans)