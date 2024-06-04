S = input().split("*")
mod = 998244353


def f(s):
    ret = 0
    for i in range(len(s)):
        ret *= 10
        ret += int(s[i])
        ret %= mod
    return ret


ans = 1
for s in S:
    ans *= f(s)
    ans %= mod
print(ans)
