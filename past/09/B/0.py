coins = [500, 100, 50, 10, 5, 1]

N = int(input())
ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    num = B - A
    for coin in coins:
        cnt = num // coin
        num -= cnt * coin
        if coin in [5, 50]:
            ans += cnt
print(ans)