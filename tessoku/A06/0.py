N, Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
for x in A:
    S.append(S[-1] + x)

for _ in range(Q):
    L, R = map(int, input().split())
    print(S[R] - S[L - 1])
