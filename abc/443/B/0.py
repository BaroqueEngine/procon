N, K = map(int, input().split())

cnt = N
ans = 0
while cnt < K:
    ans += 1
    cnt += N + ans

print(ans)