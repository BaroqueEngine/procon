X = int(input())
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        v = i * j
        if v != X:
            ans += v

print(ans)
