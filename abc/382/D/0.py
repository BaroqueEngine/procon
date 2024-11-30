import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
ans = []


def f(i, arr):
    if i == N:
        if arr[-1] <= M:
            ans.append(arr)
            return True
        else:
            return False

    cur = 1 if i == 0 else arr[-1] + 10
    ret = False
    while True:
        if f(i + 1, arr + [cur]):
            cur += 1
            ret = True
        else:
            break
    return ret


f(0, [])

ans.sort()
print(len(ans))
for x in ans:
    print(*x)
