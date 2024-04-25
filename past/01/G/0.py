import sys
sys.setrecursionlimit(10**7)

N = int(input())
S = [[0] * N for _ in range(N)]

for i in range(N - 1):
    A = list(map(int, input().split()))
    A.reverse()
    for j in range(i + 1, N):
        x = A.pop()
        S[i][j] = x
        S[j][i] = x


def calc_score(arr):
    ret = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            ret += S[arr[i]][arr[j]]
    return ret


def f(i, a, b, c):
    if i == N:
        if calc_score(a) + calc_score(b) + calc_score(c) == 60:
            print(a, b, c, calc_score(a), calc_score(b), calc_score(c))
        return calc_score(a) + calc_score(b) + calc_score(c)
    ret = -(10 ** 18)
    ret = max(ret, f(i + 1, a[:] + [i], b[:], c[:]))
    ret = max(ret, f(i + 1, a[:], b[:] + [i], c[:]))
    ret = max(ret, f(i + 1, a[:], b[:], c[:] + [i]))
    return ret


print(f(0, [], [], []))
