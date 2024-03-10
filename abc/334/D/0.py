from bisect import bisect_right
N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()

S = [0]
for x in R:
    S.append(S[-1] + x)

ans = []
for _ in range(Q):
    q = int(input())
    ans.append(bisect_right(S, q))

for x in ans:
    print(x - 1)
