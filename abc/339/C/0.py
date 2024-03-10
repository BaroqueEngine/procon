N = int(input())
A = list(map(int, input().split()))

ng = -1
ok = 10**15


def f(start):
    cur = start
    for x in A:
        cur += x
        if cur < 0:
            return False
    return True


while ok - ng > 1:
    mid = (ng + ok) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid

ans = ok
for x in A:
    ans += x
print(ans)
