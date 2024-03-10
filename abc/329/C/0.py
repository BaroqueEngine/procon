import itertools
import collections
N = int(input())
S = input()

dic = collections.defaultdict(int)

for k, g in itertools.groupby(list(S)):
    size = len(list(g))
    dic[k] = max(dic[k], size)

ans = 0
for v in dic.values():
    ans += v
print(ans)
