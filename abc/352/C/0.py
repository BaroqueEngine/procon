N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
base = 0
for x, y in A:
    base += x

ans = 0
for x, y in A:
    ans = max(ans, base - x + y)
print(ans)
