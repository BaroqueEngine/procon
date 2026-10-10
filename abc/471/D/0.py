import heapq

Q, V = map(int, input().split())
q = []
ans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        t, w = query[1:]
        heapq.heappush(q, -(w - t))
    else:
        t = query[1]
        if len(q) == 0:
            ans.append(-1)
        else:
            w = -heapq.heappop(q)
            ans.append(min(V, w + t))

for x in ans:
    print(x)
