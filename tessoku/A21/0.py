N = int(input())
P = []
A = []
for _ in range(N):
    p, a = map(int, input().split())
    p -= 1
    P.append(p)
    A.append(a)

dp = [[0] * (N + 1) for _ in range(N + 1)]

for len in range(N - 2, -1, -1):
    # [left, right]
    for left in range(N - len):
        right = left + len

        # 左を取り出した場合
        if left - 1 >= 0:
            left_score = A[left - 1] if left <= P[left - 1] <= right else 0
            dp[left][right] = max(
                dp[left][right], dp[left - 1][right] + left_score)

        # 右を取り出した場合
        if right + 1 <= N - 1:
            right_score = A[right + 1] if left <= P[right + 1] <= right else 0
            dp[left][right] = max(dp[left][right], dp[left]
                                  [right + 1] + right_score)

ans = 0
for i in range(N):
    ans = max(ans, dp[i][i])
print(ans)
