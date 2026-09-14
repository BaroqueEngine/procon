def repunit_and_pow(l, mod):
    P, R = 1, 0
    p, r = 10 % mod, 1 % mod
    while l > 0:
        if l & 1:
            R = (R * p + r) % mod
            P = (P * p) % mod
        r = (r * (p + 1)) % mod
        p = (p * p) % mod
        l >>= 1
    return P, R
K, M = map(int, input().split())
MOD = M * 10007

G = []
total_digit = 0
for _ in range(K):
    C, L = map(int, input().split())
    G.append((C, L))
    total_digit += L

ans = 0
for c, l in G:
    a = repunit_and_pow(l, MOD)[1] * c % MOD
    ans = (ans + a * pow(10, total_digit - l, MOD)) % MOD
    total_digit -= l

print(ans // M)
