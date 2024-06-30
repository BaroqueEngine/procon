import bisect
N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

L = []
R = []
for i in range(N):
    if S[i] == "0":
        L.append(X[i])
    else:
        R.append(X[i])
L.sort()

ans = 0
for r in R:
    start = bisect.bisect_left(L, r)
    end = bisect.bisect_right(L, r + T * 2)
    # print("#", r, start, end, end - start, L)
    ans += end - start

print(ans)
