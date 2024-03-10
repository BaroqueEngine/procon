def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def lcm(x, y):
    return x // gcd(x, y) * y


A, B = map(int, input().split())
print(lcm(A, B))
