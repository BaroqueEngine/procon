N, M = map(int, input().split())
S = [input(), input()]
order = [0] * (N + 1)
for _ in range(M):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    order[L] += 1
    order[R + 1] -= 1

for i in range(N):
    order[i + 1] += order[i]
    order[i] %= 2

ans = []
for i in range(N):
    ans.append(S[order[i]][i])

ans = "".join(ans)
print(ans)
