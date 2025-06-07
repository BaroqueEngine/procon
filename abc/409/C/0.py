N, L = map(int, input().split())
D = list(map(int, input().split()))

if L % 3 != 0:
    print(0)
    exit()

cnt = [0] * L
cnt[0] += 1
cur = 0
for d in D:
    cur += d
    cur %= L
    cnt[cur] += 1

ans = 0
for i in range(L):
    a = i
    b = (i + L // 3) % L
    c = (i + L // 3 * 2) % L
    ans += cnt[a] * cnt[b] * cnt[c]
    cnt[a] = 0
    cnt[b] = 0
    cnt[c] = 0

print(ans)
