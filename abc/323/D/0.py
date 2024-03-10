import heapq
N = int(input())
A = []
for _ in range(N):
    S, C = map(int, input().split())
    heapq.heappush(A, (S, C))

ans = 0
while len(A) > 0:
    size, count = heapq.heappop(A)
    while len(A) > 0 and size == A[0][0]:
        count += A[0][1]
        heapq.heappop(A)
    if count % 2 == 1:
        ans += 1
    if count >= 2:
        heapq.heappush(A, (size * 2, count // 2))
print(ans)
