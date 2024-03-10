import heapq

N, M = map(int, input().split())
people = []
for i in range(N):
    people.append(i)
heapq.heapify(people)

events = []
for _ in range(M):
    T, W, S = map(int, input().split())
    events.append((T, 1, W, S))
heapq.heapify(events)

total = [0] * N

while len(events) > 0:
    event = heapq.heappop(events)
    if event[1] == 0:
        heapq.heappush(people, (event[2]))
    else:
        if len(people) > 0:
            target = heapq.heappop(people)
            total[target] += event[2]
            heapq.heappush(events, (event[0] + event[3], 0, target))

for x in total:
    print(x)
