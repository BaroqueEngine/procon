X, C = map(int, input().split())
ans = 0
for i in range(1000, X + 1, 1000):
    tax = i / 1000 * C
    if i + tax <= X:
        ans = i

print(ans)