import heapq

N = int(input())
A = list(map(int, input().split()))

q = []
for i in range(N):
    while len(q) > 0 and q[0] < i:
        heapq.heappop(q)
    A[i] += (len(q) + i)
    heapq.heappush(q, A[i])
print(*[max(0, x - (N - 1)) for x in A])
