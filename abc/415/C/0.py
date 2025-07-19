T = int(input())

def solve():
    N = int(input())
    S = "0" + input()

    dp = [False] * (2**N)
    dp[0] = True
    for mask in range(2**N - 1):
        if dp[mask]:
            for bit in range(N):
                if mask >> bit & 1 == 0:
                    new_mask = mask | 1 << bit
                    if S[new_mask] == "0":
                        dp[new_mask] = True
    return dp[-1]
    
ans = []
for _ in range(T):
    ans.append("Yes" if solve() else "No")

for x in ans:
    print(x)
