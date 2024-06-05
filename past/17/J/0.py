N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
T = [int(input()) for _ in range(Q)]
time = set()
for a, b in P:
    time.add(a)
    time.add(b)
for t in T:
    time.add(t)
time = sorted(list(time))
time_order = {}
for i in range(len(time)):
    time_order[time[i]] = i

for i in range(N):
    P[i][0] = time_order[P[i][0]]
    P[i][1] = time_order[P[i][1]]

for i in range(Q):
    T[i] = time_order[T[i]]

MAX = len(time) + 5
schedule = [0] * MAX

for start, end in P:
    schedule[start] += 1
    schedule[end + 1] -= 1

for i in range(1, MAX):
    schedule[i] += schedule[i - 1]

for x in T:
    print(schedule[x])
