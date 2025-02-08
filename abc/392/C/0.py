N = int(input())
P = [0] + list(map(int, input().split()))
Q = [0] + list(map(int, input().split()))

see = [0] * (N + 1)
for i in range(1, N + 1):
    see[Q[i]] = i

ans = []
for i in range(1, N + 1):
    ans.append(Q[P[see[i]]])
print(*ans)