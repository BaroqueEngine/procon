import heapq

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

q = []
for i in range(N):
    heapq.heappush(q, (T[i], i))

cnt = 0
hist = [-1] * N
while cnt < N:
    time, i = heapq.heappop(q)
    if hist[i] == -1:
        hist[i] = time
        cnt += 1
    heapq.heappush(q, (time + S[i], (i + 1) % N))

for x in hist:
    print(x)
