N = int(input())
P = list(map(int, input().split()))
pos = [-1] * (N + 1)
for i in range(N):
    pos[P[i]] = i + 1

ans = []
for i in range(1, N + 1):
    ans.append(pos[i])
print(*ans)
