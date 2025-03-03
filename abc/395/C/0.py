N = int(input())
A = list(map(int, input().split()))

pos = [[] for _ in range(10**6+1)]

for i in range(N):
    pos[A[i]].append(i)

INF = 10**18
ans = INF
for g in pos:
    for i in range(len(g) - 1):
        ans = min(ans, g[i + 1] - g[i] + 1)

if ans == INF:
    ans = -1
print(ans)