N = int(input())


def f(x):
    return (x ** 3) + x >= N


ng = 0
ok = 100

while abs(ng - ok) > 0.0005:
    mid = ok + (ng - ok) / 2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)
