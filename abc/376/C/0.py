N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()


def check(A, B):
    B.sort()

    for i in range(N):
        if A[i] > B[i]:
            return False
    return True


if not check(A, B + [10**18]):
    print(-1)
    exit()

ng = 0
ok = 10**18

while ok - ng > 1:
    mid = (ok + ng) // 2
    if check(A, B + [mid]):
        ok = mid
    else:
        ng = mid

print(ok)
