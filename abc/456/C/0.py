S = input()
MOD = 998244353
ans = 0
r = 0
dup = 0
adj = False

for l in range(len(S)):
    if l - 1 >= 0 and S[l] == S[l - 1]:
        adj = False
    r = max(r, l)
    while r < len(S) and not adj:
        if r - 1 >= 0 and S[r] == S[r - 1]:
            adj = True
        r += 1

    if adj:
        dup += len(S) + 1 - r

ans = len(S) * (len(S) + 1) // 2 - dup
ans %= MOD
print(ans)