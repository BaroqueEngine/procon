import itertools
N, K = map(int, input().split())
S = input()
ans = 0

for k, g in itertools.groupby(S):
    g = list(g)
    if k == "O":
        ans += len(g) // K
print(ans)
