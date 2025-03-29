N = int(input())
P = list(map(int, input().split()))
Q = sorted(list(set(P)), reverse=True)

cnt = {}
for x in P:
    cnt[x] = cnt.get(x, 0) + 1

r = 1
rank = {}
for i in range(len(Q)):
    rank[Q[i]] = r
    r += cnt[Q[i]]

for x in P:
    print(rank[x])