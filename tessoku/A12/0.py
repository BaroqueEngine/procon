N, K = map(int, input().split())
A = list(map(int, input().split()))

ng = 0
ok = 10**9

def f(time):
    total = 0
    for x in A:
        total += time // x
    return total >= K

while ok - ng > 1:
    mid = ng + (ok - ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)