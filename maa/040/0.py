N = int(input())
A = list(map(int, input().split()))
S = [0]
for x in A:
    S.append(S[-1] + x)
M = int(input())
cur = int(input()) - 1
ans = 0
for _ in range(M - 1):
    next = int(input()) - 1
    ans += abs(S[next] - S[cur])
    cur = next
print(ans)
