def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for x in A[1:]:
    ans = gcd(ans, x)
print(ans)
