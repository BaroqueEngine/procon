N = int(input())
A = []
for _ in range(N):
    L, R = map(int, input().split())
    A.append((L, -1))
    A.append((R, 1))
A.sort()

ans = 0
cnt = 0
for _, x in A:
    x *= -1
    if (cnt + x > cnt) and (cnt != 0):
        ans += cnt
    cnt += x
print(ans)
