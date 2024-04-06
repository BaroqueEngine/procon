N, S = map(int, input().split())

cnt = 0
for red in range(1, N + 1):
    for blue in range(1, N + 1):
        if red + blue <= S:
            cnt += 1
print(cnt)
