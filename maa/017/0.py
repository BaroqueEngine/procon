def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a // gcd(a, b) * b


N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for x in A[1:]:
    ans = lcm(ans, x)
print(ans)
