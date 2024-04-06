N = int(input())
ans = []
for i in range(2, N + 1):
    if i * i > N:
        break
    while N % i == 0:
        ans.append(i)
        N //= i

if N != 1:
    ans.append(N)

print(*ans)
