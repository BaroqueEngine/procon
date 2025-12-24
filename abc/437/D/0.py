import bisect
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
SB = [0]
for x in B:
    SB.append(SB[-1] + x)

MOD = 998244353
ans = 0
for x in A:
    pos = bisect.bisect_right(B, x - 1)
    ans += x * pos - SB[pos]
    ans -= x * (M - pos) - (SB[M] - SB[pos])
    ans %= MOD

print(ans)