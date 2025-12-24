N = int(input())
A = list(map(int, input().split()))

ans = 0
cnt = 0
for x in A:
    ans += 1
    cnt = max(cnt, x - 1)
    cnt -= 1
    if cnt < 0:
        break

print(ans)