def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


A, B, C = map(int, input().split())
g = gcd(C, gcd(A, B))
print((A // g - 1) + (B // g - 1) + (C // g - 1))
