from collections import defaultdict
N, M = map(int, input().split())
cnt = [0] * (N + 1)
ids = defaultdict(int)
pair = set()

for _ in range(M):
    A, B = map(int, input().split())
    if (A, B) not in pair:
        cnt[A] += 1
        cnt[B] += 1
        pair.add((A, B))

for i in range(1, N + 1):
    ids[cnt[i]] += 1

ans = 0
for a, b in pair:
    if cnt[a] + cnt[b] == len(pair) + 1:
        ans += 1

def nc2(x):
    return x * (x - 1) // 2

for k, v in ids.items():
    l = len(pair) - k
    if k < l and k in ids and l in ids:
        ans += ids[k] * ids[l]
    if k == l:
        ans += nc2(ids[k])

for a, b in pair:
    if cnt[a] + cnt[b] == len(pair):
        ans -= 1

print(ans)


