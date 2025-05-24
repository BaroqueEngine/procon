X, Y = map(int, input().split())

a = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j >= X or abs(i - j) >= Y:
            a += 1

print(a / 36)