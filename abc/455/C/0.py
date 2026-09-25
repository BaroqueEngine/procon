from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

dic = defaultdict(int)
for x in A:
    dic[x] += 1

G = []
for k, v in dic.items():
    G.append((k * v, k))
G.sort()

for _ in range(min(K, len(G))):
    G.pop()

ans = 0
for t in G:
    ans += t[0]
print(ans)