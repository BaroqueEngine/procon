N, X = map(int, input().split())
A = list(map(int, input().split()))

ok = 0
ng = N


def f(index):
    return A[index] <= X


while ng - ok > 1:
    mid = ok + (ng - ok) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok + 1)
