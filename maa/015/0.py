def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


A, B = map(int, input().split())
print(gcd(A, B))
