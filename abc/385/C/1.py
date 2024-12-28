from itertools import groupby
N = int(input())
H = list(map(int, input().split()))
ans = 1

for i in range(1, N):
    arrs = [[] for _ in range(i)]
    for j in range(N):
        arrs[j % i].append(H[j])
    for arr in arrs:
        for _, v in groupby(arr):
            v = list(v)
            ans = max(ans, len(v))

print(ans)
