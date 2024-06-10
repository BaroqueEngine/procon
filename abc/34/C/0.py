W, H = map(int, input().split())
MOD = 10**9+7


def fact(x):
    ret = 1
    for i in range(1, x + 1):
        ret *= i
        ret %= MOD
    return ret


N = W + H - 2
R = W - 1


print((fact(N) * pow(fact(R), MOD - 2, MOD)
      * pow(fact(N - R), MOD - 2, MOD)) % MOD)
