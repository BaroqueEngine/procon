def p(k):
    return (1 + k) * k // 2


def f(k, N):
    return p(k) <= N


N = int(input())
ok = 1
ng = 10**18
while abs(ng - ok) > 1:
    mid = (ng + ok) // 2
    if f(mid, N):
        ok = mid
    else:
        ng = mid
print(ok)
