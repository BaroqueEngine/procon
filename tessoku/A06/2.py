N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [A[0]]
for x in A[1:]:
    S.append(S[-1] + x)
S.append(0)

ans = []
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    ans.append(S[R] - S[L - 1])

for x in ans:
    print(x)
