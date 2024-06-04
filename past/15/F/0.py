N = int(input())
A = list(map(int, input().split()))
SA = sorted(A)

s = {}
cur = -1
for i in range(N):
    if cur == SA[i]:
        continue
    cur = SA[i]
    s[cur] = i + 1

cnt = {}
for x in A:
    cnt[x] = 0

ans = []
for x in A:
    ans.append(s[x] + cnt[x])
    cnt[x] += 1
print(*ans)
