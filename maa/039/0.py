N, Q = map(int, input().split())
A = [0] * (N + 1)
for _ in range(Q):
    L, R, X = map(int, input().split())
    L -= 1
    R -= 1
    A[L] += X
    A[R + 1] -= X

S = [A[0]]
for x in A[1:-1]:
    S.append(S[-1] + x)

ans = ""
for i in range(N - 1):
    if S[i] == S[i + 1]:
        ans += "="
    elif S[i] < S[i + 1]:
        ans += "<"
    else:
        ans += ">"
print(ans)
