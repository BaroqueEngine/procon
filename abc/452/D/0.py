from collections import defaultdict
import bisect

S = input()
T = input()

dic = defaultdict(list)

for i, c in enumerate(S):
    dic[c].append(i)

ans = 0
for l in range(len(S)):
    r = l
    ok = True
    for c in T:
        pos = bisect.bisect_left(dic[c], r)
        if len(dic[c]) == 0 or pos == len(dic[c]):
            ok = False
            break
        r = dic[c][pos] + 1
    if ok:
        ans += (r - 1 - l)
    else:
        ans += len(S) - l


print(ans)
