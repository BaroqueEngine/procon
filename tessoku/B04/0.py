N = int(input())
ans = 0
base = 1

while N > 0:
    x = N % 10
    N //= 10
    ans += x * base
    base *= 2
print(ans)
