N = int(input())
A = list(map(int, input().split()))

ans = 0
for x in range(N + 1):
    cnt = 0
    for y in A:
        if y >= x:
            cnt += 1
    if cnt >= x:
        ans = max(ans, x)

print(ans)