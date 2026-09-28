import heapq

N = int(input())
q = []
for _ in range(N):
    H, L = map(int, input().split())
    heapq.heappush(q, (-H, L))

Q = int(input())
T = list(map(int, input().split()))
ST = sorted(T)

ans = {}

for time in ST:
    while True:
        if time < q[0][1]:
            ans[time] = -q[0][0]
            break
        heapq.heappop(q)

for time in T:
    print(ans[time])
