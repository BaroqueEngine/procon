N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

import bisect

ng = -1
ok = 10**10


def f(price):
    x = bisect.bisect_right(A, price)
    y = M - bisect.bisect_left(B, price)

    return x >= y


while abs(ok - ng) > 1:
    mid = (ok + ng) // 2

    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)
