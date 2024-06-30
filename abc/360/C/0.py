N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

for i in range(N):
    A[i] -= 1

G = [[] for _ in range(N)]
for i in range(N):
    G[A[i]].append(i)

ans = 0
for g in G:
    if len(g) < 2:
        continue
    max_weight = 0
    weights = 0
    for i in g:
        weights += W[i]
        max_weight = max(max_weight, W[i])
    ans += weights - max_weight
print(ans)
