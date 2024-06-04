import decimal

N = int(input())
A = list(map(int, input().split()))
max_v = max(A)

ans = []
for x in A:
    ans.append(decimal.Decimal((10**9) * x /
               max_v).quantize(decimal.Decimal("0"), decimal.ROUND_HALF_UP))
print(*ans)
