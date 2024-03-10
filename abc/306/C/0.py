N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

cnt = defaultdict(int)
ans = []

for x in A:
    cnt[x] += 1
    if cnt[x] == 2:
        ans.append(x)

print(*ans)
