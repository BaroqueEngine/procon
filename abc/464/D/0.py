T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = input()
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    # dp[i][晴, 雨]
    dp = [[0, 0] for _ in range(N)]
    dp[0][0] -= (0 if S[0] == "S" else X[0])
    dp[0][1] -= (0 if S[0] == "R" else X[0])

    for i in range(1, N):
        sunny = max(
            dp[i - 1][0],            # 昨日、晴 -> 今日、晴
            dp[i - 1][1] + Y[i - 1], # 昨日、雨 -> 今日、晴
        )

        rainy = max(
            dp[i - 1][0],            # 昨日、晴 -> 今日、雨
            dp[i - 1][1],            # 昨日、雨 -> 今日、雨
        )

        dp[i][0] = sunny - (0 if S[i] == "S" else X[i])
        dp[i][1] = rainy - (0 if S[i] == "R" else X[i])

    ans.append(max(dp[-1]))

for x in ans:
    print(x)
