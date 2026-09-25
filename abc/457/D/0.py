N, K = map(int, input().split())
A = list(map(int, input().split()))

ok = min(A)
ng = 10**19

def f(target):
    cnt = K
    for i in range(N):
        if target > A[i]:
            diff = target - A[i]
            cnt -= (diff + i) // (i + 1)
    return cnt >= 0

while ng - ok > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)