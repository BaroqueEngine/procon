N, K = map(int, input().split())
A = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append((a, b))

ans = 0
for i in range(1, 101):
    for j in range(1, 101):
        cnt = 0
        for a, b in A:
            if 0 <= a - i <= K and 0 <= b - j <= K:
                cnt += 1
        ans = max(ans, cnt)

print(ans)