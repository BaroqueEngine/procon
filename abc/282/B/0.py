N, M = map(int, input().split())


def calc_score(s):
    s = list(s)
    k = 1
    ret = 0
    while len(s) > 0:
        if s[-1] == "o":
            ret += k
        k *= 2
        s.pop()
    return ret


score = [calc_score(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if (score[i] | score[j]) == 2**M - 1:
            ans += 1
print(ans)
