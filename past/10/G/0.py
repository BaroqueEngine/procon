a, b, c = map(int, input().split())

ng = 1
ok = 2


def f(x):
    y = a * (x ** 5) + b * x + c
    return y >= 0


for i in range(1000):
    mid = (ng + ok) / 2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)
