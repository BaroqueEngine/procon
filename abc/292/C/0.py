N = int(input())

dic = [0] * (N + 1)

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a * b > N:
            break
        dic[a * b] += 1

ans = 0
for i in range(1, N):
    ans += dic[i] * dic[N - i]
print(ans)
