import heapq
N, K = map(int, input().split())
total = 0
time = 0

q = []
ans = [] # (帰る時刻, 人数)
for _ in range(N):
    A, B, C = map(int, input().split())
    while total + C > K:
        leave_time, num = heapq.heappop(q)
        total -= num
        time = max(time, leave_time)
    time = max(time, A)
    ans.append(time)
    total += C
    heapq.heappush(q, (time + B, C))

for x in ans:
    print(x)