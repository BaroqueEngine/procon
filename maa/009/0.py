N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (S + 1)
dp[0] = True

for x in A:
    idp = dp[:]
    for i in range(0, S + 1):
        if dp[i] and i + x <= S:
            idp[i + x] = True
    dp = idp[:]

print("Yes" if dp[S] else "No")
