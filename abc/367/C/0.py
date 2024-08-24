import sys
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
R = list(map(int, input().split()))

ans = []


def f(arr, pos):
    if pos == N:
        if sum(arr) % K == 0:
            ans.append(" ".join(map(str, arr)))
        return

    for i in range(1, R[pos] + 1):
        new_arr = arr[:]
        new_arr.append(i)
        f(new_arr, pos + 1)


f([], 0)
ans.sort()

for line in ans:
    print(line)
