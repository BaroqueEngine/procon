N = int(input())
S = input()

dp = [[False] * 10 for _ in range(N + 1)]
dp[0][0] = True
prev = [[(-1, -1)] * 10 for _ in range(N + 1)]

for i in range(N):
    for x in range(10):
        if S[i] in ["?", str(x)]:
            for a in range(10):
                if dp[i][a]:
                    b = a + (i + 1) * x
                    b %= 10
                    dp[i + 1][b] = True
                    prev[i + 1][b] = (a, x)

if not dp[-1][0]:
    print("No")
    exit()

ans = ""
cur = 0
for i in range(N, 0, -1):
    cur, x = prev[i][cur]
    ans += str(x)
print("Yes")
print(ans[::-1])
