N = int(input())
H = list(map(int, input().split()))
ans = 1

for step in range(1, N):
    for start in range(N):
        cnt = 0
        for pos in range(start, N, step):
            if H[start] != H[pos]:
                break
            cnt += 1
        ans = max(ans, cnt)
print(ans)
