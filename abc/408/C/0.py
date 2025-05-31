N, M = map(int, input().split())
P = [0] * (N + 1)
for _ in range(M):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    P[L] += 1
    P[R + 1] -= 1

S = []
cur = 0
for i in range(N):
    cur += P[i]
    S.append(cur)

print(min(S))