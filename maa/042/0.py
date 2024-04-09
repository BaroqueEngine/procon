N = int(input())
cnt = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        cnt[j] += 1

ans = 0
for i in range(1, N + 1):
    ans += i * cnt[i]
print(ans)
