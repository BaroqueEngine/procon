import sys
N = int(input())
G = [[] for _ in range(N)]
P = [-1] + list(map(int, input().split()))
S = input().split()
mod = 998244353

for cur in range(1, N):
    par = P[cur] - 1
    G[par].append(cur)

sys.setrecursionlimit(10**7)


def f(cur):
    if len(G[cur]) == 2:
        left = G[cur][0]
        right = G[cur][1]
        if S[cur] == "+":
            ret = f(left) + f(right)
        else:
            ret = f(left) * f(right)
    else:
        ret = int(S[cur])
    return ret % mod


print(f(0))
