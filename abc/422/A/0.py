S = input()
A, B = map(int, S.split("-"))
B += 1
if B == 9:
    B = 1
    A += 1
print(f"{A}-{B}")