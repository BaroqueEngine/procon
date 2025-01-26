import sys
sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))
ans = set([])

def calc_xor(arr):
    total = 0
    for x in arr:
        total ^= x
    return total

def f(i, arr):
    if i == N:
        ans.add(calc_xor(arr))
        return
    f(i + 1, arr + [A[i]])
    for j in range(len(arr)):
        arr[j] += A[i]
        f(i + 1, arr)
        arr[j] -= A[i]


f(0, [])
print(len(ans))