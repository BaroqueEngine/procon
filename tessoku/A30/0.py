n, r = map(int, input().split())
mod = 10**9+7


def fact(x):
    ret = 1
    for i in range(1, x + 1):
        ret *= i
        ret %= mod
    return ret


def inv(x):
    return pow(x, mod - 2, mod)


print(fact(n) * inv(fact(r) * fact(n - r)) % mod)
