import sys
sys.setrecursionlimit(10**4)
N, K, P = map(int, input().split())
INF = 10**15
dic = {}

indexes = []


def f(i, arr):
    if i == K:
        dic[tuple(arr)] = INF
        indexes.append(tuple(arr))
        return
    for j in range(6):
        f(i + 1, arr + [j])


f(0, [])

indexes.sort(reverse=True)
dic[tuple([0] * K)] = 0


def create_param(a, b):
    arr = []
    for i in range(len(a)):
        arr.append(min(a[i] + b[i], 5))
    return tuple(arr)


for _ in range(N):
    c = list(map(int, input().split()))
    cur_cost, cur_param = c[0], c[1:]
    for param in indexes:
        if dic[param] == INF:
            continue
        new_param = create_param(cur_param, param)
        if dic[param] + cur_cost < dic[new_param]:
            dic[new_param] = dic[param] + cur_cost

ans = INF


def g(i, arr):
    global ans
    if i == K:
        ans = min(ans, dic[tuple(arr)])
        return
    for j in range(P, 6):
        g(i + 1, arr + [j])


g(0, [])

if ans == INF:
    ans = -1
print(ans)
