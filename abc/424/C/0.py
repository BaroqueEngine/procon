from collections import deque

N = int(input())
learned = [False] * N
nexts = [set([]) for _ in range(N)]
queue = deque([])

for i in range(N):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        queue.append(i)
    else:
        A -= 1
        B -= 1
        nexts[A].add(i)
        nexts[B].add(i)

while len(queue) > 0:
    cur = queue.popleft()
    if learned[cur]:
        continue
    learned[cur] = True
    for next in nexts[cur]:
        queue.append(next)

print(sum(learned))