N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for x in A:
    ans.append(min(max(x, L), R))
print(*ans)
