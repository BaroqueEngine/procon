import sys
sys.setrecursionlimit(10**7)

g = []


def f(arr):
    g.append(int("".join(map(str, arr))))
    for i in range(0, 10):
        if arr[-1] > i:
            f(arr + [i])


for i in range(1, 10):
    f([i])


g.sort()
K = int(input())
print(g[K - 1])
