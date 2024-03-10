MOD = 10**9 + 7
A, B = map(int, input().split())

ans = 1
while B > 0:
    if B % 2 == 0:
        ans = (ans * A) % MOD
    else:
        ans = ((ans * A) + A) % MOD
    B //= 2

print(ans)

# NG
