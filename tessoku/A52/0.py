Q = int(input())

import queue

q = queue.Queue()
for _ in range(Q):
    t = input().split()
    if t[0] == "1":
        q.put(t[1])
    elif t[0] == "2":
        print(q.queue[0])
    else:
        q.get()
