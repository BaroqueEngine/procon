from sortedcontainers import SortedSet
N, K = map(int, input().split())
A = list(map(int, input().split()))
pos = [None] * (N + 1)

for i in range(1, N + 1):
    pos[A[i - 1]] = i

S = SortedSet([])
ans = 10**18
for i in range(1, K + 1):
    S.add(pos[i])
ans = min(ans, S[-1] - S[0])

for i in range(2, N - K + 2):
    S.add(pos[i + K - 1])
    S.discard(pos[i - 1])
    ans = min(ans, S[-1] - S[0])
print(ans)
