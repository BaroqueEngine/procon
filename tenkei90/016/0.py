N = int(input())
A, B, C = map(int, input().split())

ans = 10**18
for i in range(10000):
    if A * i > N:
        break
    for j in range(10000 - i):
        cost = N - A * i - B * j
        if cost < 0:
            break
        if cost % C != 0:
            continue
        k = cost // C
        ans = min(ans, i + j + k)
print(ans)