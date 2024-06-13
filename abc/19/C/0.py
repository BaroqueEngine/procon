from functools import cache
N = int(input())
A = list(map(int, input().split()))


@cache
def f(x):
    while x > 1 and x % 2 == 0:
        x //= 2
    return x


for i in range(N):
    A[i] = f(A[i])

print(len(set(A)))
