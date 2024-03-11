T = input()
N = int(input())
W = [input().split()[1:] for _ in range(N)]

INF = 10**18
dp = [INF] * (len(T) + 1)
dp[0] = 0

for words in W:
    idp = dp[:]
    for word in words:
        for i in range(len(T)):
            if dp[i] == INF:
                continue
            if i + len(word) > len(T):
                continue
            if T[i:i+len(word)] != word:
                continue
            idp[i+len(word)] = min(idp[i+len(word)], dp[i] + 1)
    dp = idp[:]

if dp[-1] == INF:
    dp[-1] = -1
print(dp[-1])
