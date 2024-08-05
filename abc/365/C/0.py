N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= M:
    print("infinite")
    exit()

ok = 1
ng = 10**20


def f(target):
    total = 0
    for x in A:
        total += min(x, target)
    return total <= M


while ng - ok > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)
