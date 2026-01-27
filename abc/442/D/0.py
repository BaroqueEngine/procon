N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
for x in A:
    S.append(S[-1] + x)

ans = []
for i in range(Q):
    T = list(map(int, input().split()))
    if T[0] == 1:
        x = T[1] - 1
        S[x + 1] -= A[x]
        S[x + 1] += A[x + 1]
        A[x], A[x + 1] = A[x + 1], A[x]
    else:
        l = T[1] - 1
        r = T[2] - 1
        ans.append(S[r + 1] - S[l])

for x in ans:
    print(x)