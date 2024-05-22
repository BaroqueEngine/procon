import sys
sys.setrecursionlimit(10**7)

A, B = map(int, input().split())

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    return x // gcd(x, y) * y

ans = lcm(A, B)
if ans > 10**18:
    ans = "Large"
print(ans)