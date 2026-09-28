N, D = map(int, input().split())
A = []
max_t = 0
for _ in range(N):
    S, T = map(int, input().split())
    A.append((S, T))
    max_t = max(max_t, T)

imos = [0] * (max_t + 1)
for s, t in A:
    if t - s >= D:
        imos[s] += 1
        imos[t - D + 1] -= 1

for i in range(len(imos) - 1):
    imos[i + 1] += imos[i]

def nc2(x):
    return x * (x - 1) // 2

ans = 0
for i in range(len(imos)):
    ans += nc2(imos[i])

print(ans)