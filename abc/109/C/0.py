N, S = map(int, input().split())
X = list(map(int, input().split()))
for i in range(N):
    X[i] = abs(X[i] - S)


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


ans = X[0]
for x in X[1:]:
    ans = gcd(ans, x)
print(ans)
