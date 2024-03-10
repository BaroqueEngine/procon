import sys
R = []
for i in range(1, 13):
    R.append(int(str(1) * i))

s = set()

sys.setrecursionlimit(10**7)


def f(arr):
    if len(arr) == 3:
        s.add(sum(arr))
        return

    for r in R:
        arr.append(r)
        f(arr)
        arr.pop()


f([])

arr = sorted(list(s))

N = int(input())
print(arr[N - 1])
