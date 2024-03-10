N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (S + 1)
dp[0] = True

for i in range(N):
    idp = dp[:]
    for j in range(S, -1, -1):
        if j - A[i] >= 0:
            idp[j] |= idp[j - A[i]]
    dp = idp[:]

print("Yes" if dp[S] else "No")
