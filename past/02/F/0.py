import heapq
N = int(input())
date = [[] for _ in range(N + 1)]
for _ in range(N):
    A, B = map(int, input().split())
    date[A].append(B)

q = []
ans = 0
for i in range(1, N + 1):
    for x in date[i]:
        heapq.heappush(q, -x)
    ans += -heapq.heappop(q)
    print(ans)
