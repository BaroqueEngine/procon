N = int(input())
A = list(map(int, input().split()))
G = {}
for i in range(N):
    G[i + 1] = A[i]

seen = [False] * (N + 1)

import sys

sys.setrecursionlimit(10**7)


def search(cur, routes, st: set):
    seen[cur] = True
    routes += [cur]
    st.add(cur)

    next = G[cur]
    if next in st:
        for i in range(len(routes)):
            if routes[i] == next:
                print(len(routes) - i)
                print(*routes[i:])
                exit()
    elif not seen[next]:
        search(next, routes, st)


for i in range(1, N + 1):
    if seen[i]:
        continue
    search(i, [], set())
