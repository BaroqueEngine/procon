N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for x in A:
    if x % K == 0:
        ans.append(x // K)
print(*ans)
