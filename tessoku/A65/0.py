N = int(input())
A = list(map(int, input().split()))
A = [0] + [x - 1 for x in A]
ans = [-1] * N
childs = [[] for _ in range(N)]
for i in range(1, N):
    childs[A[i]].append(i)

import sys

sys.setrecursionlimit(10**9)


def search_childs(cur):
    if ans[cur] != -1:
        return ans[cur]
    num = 0
    for child in childs[cur]:
        num += search_childs(child)
    ans[cur] = num

    return num + 1


for i in range(N):
    search_childs(i)
    print(ans[i])
