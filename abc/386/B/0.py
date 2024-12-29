from itertools import groupby

ans = 0
S = input()

for k, v in groupby(S):
    l = len(list(v))
    if k != "0":
        ans += l
    else:
        ans += l // 2
        ans += l % 2

print(ans)
