import heapq

Q = int(input())
q = []
ans = []
for _ in range(Q):
    kind, h = map(int, input().split())
    if kind == 1:
        heapq.heappush(q, h)
    else:
        while len(q) > 0 and q[0] <= h:
            heapq.heappop(q)
    ans.append(len(q))

for x in ans:
    print(x)