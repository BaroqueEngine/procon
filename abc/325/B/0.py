N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


def f(time):
    ret = 0
    for w, x in A:
        t = (time + x) % 24
        if 9 <= t <= 17:
            ret += w
    return ret


ans = 0
for time in range(24):
    ans = max(ans, f(time))
print(ans)
