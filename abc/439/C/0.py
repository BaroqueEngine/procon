N = int(input())

cnt = [0] * (N + 1)

for x in range(1, 3200):
    for y in range(x + 1, 3200):
        z = x * x + y * y
        if z <= N:
            cnt[z] += 1

ans = []
for i in range(N + 1):
    if cnt[i] == 1:
        ans.append(i)

print(len(ans))
print(*ans)