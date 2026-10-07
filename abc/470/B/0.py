from collections import defaultdict

N = int(input())
C = list(map(int, input().split()))

cnt = defaultdict(int)
max_cnt = 0

for x in C:
    cnt[x] += 1
    max_cnt = max(max_cnt, cnt[x])

print(N - max_cnt)
