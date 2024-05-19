import sys
sys.setrecursionlimit(10**7)

N = int(input())
P = [tuple(list(map(int, input().split()))) for _ in range(N)]
INF = 10**18

memo = [None] * (2**18+10)


def f(sente, used):
    if memo[used] != None:
        return memo[used]
    found = False
    results = []
    for i in range(N):
        if used >> i & 1 == 1:
            continue
        for j in range(i + 1, N):
            if used >> j & 1 == 1:
                continue
            for k in range(2):
                if P[i][k] == P[j][k]:
                    found = True
                    used |= 2 ** i
                    used |= 2 ** j
                    results.append(f(not sente, used))
                    used -= 2 ** i
                    used -= 2 ** j

    if not found:
        memo[used] = not sente
    else:
        if sente:
            memo[used] = sente in results
        else:
            memo[used] = (not sente in results)
    return memo[used]


print("Takahashi" if f(True, 0) else "Aoki")
