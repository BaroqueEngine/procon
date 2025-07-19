H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
P = list(map(int, input().split()))

ng = -1
ok = sum(P)

def f(money):
    dp = [[0] * W for _ in range(H)]
    updated = [[False] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if x == 0 and y == 0:
                new_money = money + A[0][0] - P[0] 
                if new_money >= 0:
                    dp[0][0] = new_money
                    updated[0][0] = True
            else:
                if y - 1 >= 0 and updated[y - 1][x]:
                    money = dp[y - 1][x]
                    new_money = money + A[y][x] - P[x + y]
                    if new_money >= 0:
                        dp[y][x] = new_money
                        updated[y][x] = True
                if x - 1 >= 0 and updated[y][x - 1]:
                    money = dp[y][x - 1]
                    new_money = money + A[y][x] - P[x + y]
                    if new_money >= 0:
                        dp[y][x] = max(dp[y][x], new_money)
                        updated[y][x] = True
    return updated[-1][-1]

while ok - ng > 1:
    mid = ng + (ok - ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)
