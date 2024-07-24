from more_itertools import distinct_permutations

N, K = map(int, input().split())
S = input()
ans = 0

for s in distinct_permutations(S):
    s = "".join(s)
    ok = True
    for i in range(N - K + 1):
        t = s[i:i+K]
        if t == t[::-1]:
            ok = False
            break
    if ok:
        ans += 1

print(ans)
