import collections
N = int(input())
A = list(map(int, input().split()))
B = sorted(list(set(A[:])))
total = sum(A)

cnt = collections.defaultdict(int)
for x in A:
    cnt[x] += 1

ans = collections.defaultdict(int)

for x in B:
    total -= cnt[x] * x
    ans[x] = total

for x in A:
    print(ans[x])
