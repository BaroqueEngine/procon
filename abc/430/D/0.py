from sortedcontainers import SortedSet

N = int(input())
X = list(map(int, input().split()))

INF = 10**18
st = SortedSet()
st.add(0)

min_dists = {
    0: 0
}

total = 0

def update(pos):
    new_dist = INF
    if pos - 1 >= 0:
        new_dist = min(new_dist, st[pos] - st[pos - 1])
    if pos + 1 < len(st):
        new_dist = min(new_dist, st[pos + 1] - st[pos])
    if new_dist == INF:
        new_dist = 0
    
    ret = new_dist - min_dists[st[pos]]
    min_dists[st[pos]] = new_dist
    return ret

ans = []
for x in X:
    st.add(x)
    pos = st.bisect_left(x)
    min_dists[x] = 0

    if pos - 1 >= 0:
        total += update(pos - 1)
    total += update(pos)
    if pos + 1 < len(st):
        total += update(pos + 1)
    ans.append(total)

for x in ans:
    print(x)