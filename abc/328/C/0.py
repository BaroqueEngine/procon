N, Q = map(int, input().split())
S = input()
A = [0]
for i in range(1, N):
    if S[i - 1] == S[i]:
        A.append(A[-1] + 1)
    else:
        A.append(A[-1])

ans = []
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    ans.append(A[R] - A[L])

for x in ans:
    print(x)
