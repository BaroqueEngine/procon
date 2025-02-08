N, M = map(int, input().split())
A = list(map(int, input().split()))
seen = [False] * (N + 1)
for x in A:
    seen[x] = True

ans = []
for i in range(1, N + 1):
    if not seen[i]:
        ans.append(i)
print(len(ans))
print(*ans)