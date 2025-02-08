N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

see = [0] * N
for i in range(N):
    see[Q[i] - 1] = i

ans = []
for i in range(N):
    ans.append(Q[P[see[i]] - 1])
print(*ans)