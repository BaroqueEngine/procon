import bisect
N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
total_a = sum(A)
SA = [0]
for x in A:
    SA.append(SA[-1] + x)
ans = []

def f(x, b):
    start = bisect.bisect_left(A, b)
    x -= SA[start]
    if x <= 0:
        return False
    x -= (N - start) * (b - 1)
    return x > 0

for _ in range(Q):
    B = int(input())

    if A[-1] < B:
        ans.append(-1)
        continue

    ng = 0
    ok = total_a + 1
    while (ok - ng) > 1:
        mid = ng + (ok - ng) // 2
        if f(mid, B):
            ok = mid
        else:
            ng = mid
    
    ans.append(ok if ok != total_a + 1 else -1)

for x in ans:
    print(x)