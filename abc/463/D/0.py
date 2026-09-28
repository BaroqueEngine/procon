N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort(key=lambda x: x[1])

def f(score):
    cur_r = A[0][1]
    cnt = 1
    for i in range(1, N):
        next_l, next_r = A[i]
        if next_l <= cur_r <= next_r:
            continue
        if next_l - cur_r < score:
            continue
        cur_r = next_r
        cnt += 1
    return cnt >= K

ok = 0
ng = 10**10

while ng - ok > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid

if ok == 0:
    ok = -1
print(ok)