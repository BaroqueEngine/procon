from decimal import Decimal, ROUND_HALF_UP

A, B = map(int, input().split())
x = Decimal(A / B)
print(x.quantize(Decimal("1"), rounding=ROUND_HALF_UP))