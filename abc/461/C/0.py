from collections import defaultdict
N, K, M = map(int, input().split())
dic = defaultdict(list)
items = []
for i in range(N):
    C, V = map(int, input().split())
    dic[C].append((V, i))
    items.append((V, i))

items.sort()
selected = set()
color_tops = []

for k in dic:
    dic[k].sort()
    color_tops.append(dic[k][-1])

color_tops.sort()

ans = 0

for _ in range(M):
    v, i = color_tops.pop()
    ans += v
    selected.add(i)

while len(selected) < K:
    while True:
        v, i = items.pop()
        if i not in selected:
            ans += v
            selected.add(i) # 不要かも
            break

print(ans)
