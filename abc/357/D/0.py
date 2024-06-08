import sys
sys.setrecursionlimit(10**7)
MOD = 998244353
A = int(input())
R = pow(10, len(str(A)), MOD)
N = A - 1

up = (A * (1 - pow(R, N + 1, MOD)) % MOD)
down = pow(1 - R, -1, MOD)
print((up * down) % MOD)
