N, M, Q = map(int, input().split())
solved = [[] for _ in range(N + 1)]
cnt = [0] * (N + 1)

ans = []
for _ in range(Q):
    T = list(map(int, input().split()))
    if T[0] == 1:
        n = T[1]
        score = 0
        for p in solved[n]:
            score += N - cnt[p]
        ans.append(score)
    else:
        n, m = T[1:]
        cnt[m] += 1
        solved[n].append(m)

for x in ans:
    print(x)
