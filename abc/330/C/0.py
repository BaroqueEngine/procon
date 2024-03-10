import math

D = int(input())

ans = 10**18
for x in range(0, 1420000):
    a = abs(x * x - D)
    b = math.floor(math.sqrt(a))
    b = max(b - 1, 0)
    for y in range(b - 5, b + 5):
        y = max(y, 0)
        ans = min(ans, abs(x * x + y * y - D))
print(ans)
