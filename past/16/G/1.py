import sys


def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (c + a > b)


N = int(input())
A = list(map(int, input().split()))

sys.setrecursionlimit(10**7)


def f(arr):
    if len(arr) == 0:
        return 1
    ret = 0
    i = 0
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if is_triangle(arr[i], arr[j], arr[k]):
                ret += f(arr[i + 1: j] + arr[j + 1: k] + arr[k + 1:])
    return ret


print(f(A))
