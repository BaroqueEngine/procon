N = int(input())
A = list(map(int, input().split()))
A.sort()

from itertools import groupby


def f(x):
    if x < 3:
        return 0
    return x * (x - 1) * (x - 2) // 6


ans = 0
for (
    key,
    group,
) in groupby(A):
    ans += f(len(list(group)))

print(ans)
