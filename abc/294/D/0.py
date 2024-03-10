N, Q = map(int, input().split())

wait = [x + 1 for x in range(N)]
wait.reverse()

import heapq

called = []

done = set()

ans = []

for _ in range(Q):
    x = input()
    if x == "1":
        cur = wait.pop()
        heapq.heappush(called, cur)
    elif x[0] == "2":
        cur = int(x.split()[1])
        done.add(cur)
    else:
        while True:
            if called[0] not in done:
                ans.append(called[0])
                break
            else:
                heapq.heappop(called)

for x in ans:
    print(x)
