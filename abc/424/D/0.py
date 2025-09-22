T = int(input())
ans = []

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    masks = []
    for s in S:
        mask = 0
        for i in range(W):
            if s[i] == "#":
                mask += 2 ** i
        masks.append(mask)
    
    INF = 10**18
    dp = [INF] * (2 ** W)
    for i in range(2 ** W):
        dp[i] = bin(masks[0] & ~i).count("1")
    
    for i in range(1, H):
        new_dp = [INF] * (2 ** W)
        for current in range(2 ** W):
            cost = bin(masks[i] & ~current).count("1")
            for prev in range(2 ** W):
                if dp[prev] == INF:
                    continue

                ok = True
                for j in range(W - 1):
                    if (prev >> j) & 3 == (current >> j) & 3 == 3:
                        ok = False
                if ok:
                    new_dp[current] = min(new_dp[current], dp[prev] + cost)
        dp = new_dp
    
    return min(dp)


for _ in range(T):
    ans.append(solve())

for x in ans:
    print(x)