N = int(input())
ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    if A < B:
        ans += 1

print(ans)