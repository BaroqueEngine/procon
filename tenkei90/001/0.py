N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

ok = 1
ng = 10**18

def f(score):
    cnt = 0
    prev = 0
    for x in A:
        if x - prev >= score:
            cnt += 1
            prev = x
    if L - prev >= score:
        cnt += 1
    return cnt >= K + 1    

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)