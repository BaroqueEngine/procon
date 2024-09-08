import itertools

N = int(input())
A = list(map(int, input().split()))
D = [A[i + 1] - A[i] for i in range(N - 1)]


def f(x):
    return x * (x - 1) // 2


ans = N

for key, arr in itertools.groupby(D):
    arr = list(arr)
    ans += f(len(arr) + 1)

print(ans)
