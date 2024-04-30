import collections
N, Q = map(int, input().split())
prev = collections.defaultdict(int)
next = collections.defaultdict(int)
top = collections.defaultdict(int)
INF = 10**18

for i in range(1, N + 1):
    prev[-i] = i
    prev[i] = INF
    next[i] = -i
    top[i] = i

for _ in range(Q):
    f, t, x = map(int, input().split())
    f_top_x = top[f]
    prev[next[x]] = None
    top[f] = next[x]
    next[x] = top[t]
    top[t] = f_top_x
    
pos = [None] * (N + 1)
for i in range(1, N + 1):
    x = top[i]
    while x >= 1:
        pos[x] = i
        x = next[x]

for x in pos[1:]:
    print(x)
