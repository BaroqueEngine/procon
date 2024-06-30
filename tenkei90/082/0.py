L, R = map(int, input().split())
MOD = 10**9+7


def get_digit_last(digit):
    return int("9" * digit)


def f(l, r):
    num = r - l + 1
    digit = len(str(l))
    return (l + r) * num // 2 * digit


ans = 0
i = L
while i <= R:
    if len(str(i)) == len(str(R)):
        last = R
    else:
        last = get_digit_last(len(str(i)))
    ans += f(i, last)
    ans %= MOD
    i = last + 1

print(ans)
