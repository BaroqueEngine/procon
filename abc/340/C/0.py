import sys
import functools
N = int(input())

sys.setrecursionlimit(10**7)


@functools.cache
def f(x):
    ret = 0
    if x >= 2:
        ret += x
        ret += f(x // 2)
        ret += f(x // 2 if x % 2 == 0 else x // 2 + 1)
    return ret


print(f(N))
