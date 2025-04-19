import queue
q = queue.Queue()
Q = int(input())
ans = []
for _ in range(Q):
    T = list(map(int, input().split()))
    if T[0] == 1:
        q.put(T[1])
    else:
        ans.append(q.get())

for x in ans:
    print(x)