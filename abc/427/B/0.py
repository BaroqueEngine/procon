def f(x):
    ret = 0
    while x > 0:
        ret += x % 10
        x //= 10
    return ret

N = int(input())
ans = 1

for i in range(N - 1):
    ans += f(ans)

print(ans)