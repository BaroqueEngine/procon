MOD = 10**9 + 7
A, B = map(int, input().split())


def f(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return (f(a, b // 2) ** 2) % MOD
    else:
        return ((f(a, b // 2) ** 2) * a) % MOD


print(f(A, B))
