N, Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
for x in A:
    S.append(S[-1] + x)

for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    print(S[R + 1] - S[L])
