import sys
mod = 10**9+7
a, b = map(int, input().split())

sys.setrecursionlimit(10**7)


def f(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return f(a * a % mod, b // 2)
    else:
        return f(a, b - 1) * a % mod


print(f(a, b))
