N = int(input())
A = list(map(int, input().split()))
K = int(input())

ans = 0
for x in A:
    if K <= x:
        ans += 1

print(ans)