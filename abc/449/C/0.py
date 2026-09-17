import bisect
from collections import defaultdict

N, L, R = map(int, input().split())
S = input()
dic = defaultdict(list)
for i, c in enumerate(S):
    dic[c].append(i)

ans = 0
for pos in dic.values():
    for i in range(len(pos)):
        left = bisect.bisect_left(pos, pos[i] + L)
        right = bisect.bisect_right(pos, pos[i] + R)
        ans += right - left

print(ans)