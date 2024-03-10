N, X = map(int, input().split())
T = []
for _ in range(N):
    A, B = map(int, input().split())
    T.append((A, B))

dp = [False] * (X + 1)
dp[0] = True

for a, b in T:
    for _ in range(b):
        idp = dp[:]
        for i in range(X - 1, -1, -1):
            if idp[i] and i + a <= X:
                idp[i + a] = True
        dp = idp[:]

print("Yes" if dp[X] else "No")
