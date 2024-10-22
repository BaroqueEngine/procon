N, C = map(int, input().split())
T = list(map(int, input().split()))

ans = 0
prev = -10**18

for x in T:
    if x - prev >= C:
        ans += 1
        prev = x

print(ans)
