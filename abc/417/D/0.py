import bisect

N = int(input())
P = []
A = []
B = []

for _ in range(N):
    X = list(map(int, input().split()))
    P.append(X[0])
    A.append(X[1])
    B.append(X[2])

MAX = max(P) + max(A) + 1
# dp[i][j] = i番目までのプレゼントを貰った状態で、テンションjのときの最終的なテンション
dp = [[0] * MAX for _ in range(N + 1)]

for j in range(MAX):
    dp[-1][j] = j

for i in range(N - 1, -1, -1):
    for j in range(MAX):
        if P[i] >= j:
            dp[i][j] = dp[i + 1][j + A[i]]
        else:
            dp[i][j] = dp[i + 1][max(j - B[i], 0)]

SB = [0]
for x in B:
    SB.append(SB[-1] + x)

ans = []
Q = int(input())
for _ in range(Q):
    X = int(input())

    if X < MAX:
        ans.append(dp[0][X])
    else:
        target = X - MAX
        index = bisect.bisect_right(SB, target)

        if index > N:
            ans.append(X - SB[-1])
        else:
            X = max(X - SB[index], 0)
            ans.append(dp[index][X])

for x in ans:
    print(x)