def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


A, B = map(int, input().split())
print(gcd(A, B))
