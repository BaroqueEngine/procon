import collections
N = int(input())
A = list(map(int, input().split()))


def f(x):
    return x * (x - 1) // 2


c = collections.Counter(A)
print(f(c[1]) + f(c[2]) + f(c[3]))
