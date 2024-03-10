N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
A.sort(key=lambda x: x[1])

ans = 0
time = -1

for l, r in A:
    if time <= l:
        time = r
        ans += 1
print(ans)
