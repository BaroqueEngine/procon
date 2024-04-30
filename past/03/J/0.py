import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
D = [0] * N
D[0] = -A[0]
ans = []
ans.append(1)
for x in A[1:]:
    pos = bisect.bisect_right(D, -x)
    if pos >= N:
        ans.append(-1)
    else:
        ans.append(pos + 1)
        D[pos] = -x
for x in ans:
    print(x)