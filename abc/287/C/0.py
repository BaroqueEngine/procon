N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    G[U].append(V)
    G[V].append(U)

start = None
cnt_one = 0
for i in range(N):
    if not len(G[i]) == 1 and not len(G[i]) == 2:
        print("No")
        exit()
    if len(G[i]) == 1:
        cnt_one += 1
        start = i

if cnt_one != 2:
    print("No")
    exit()

cur = start
seen = [False] * N
seen[cur] = True

while True:
    prev_cur = cur
    for next in G[cur]:
        if seen[next]:
            continue
        cur = next
        seen[next] = True

    if prev_cur == cur:
        break

print("Yes" if sum(seen) == N else "No")
