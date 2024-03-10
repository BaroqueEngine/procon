N = int(input())
A = list(map(int, input().split()))
order = [-1] * N

start = -1
for i in range(N):
    prev = A[i]
    if prev != -1:
        order[prev - 1] = i
    else:
        start = i

ans = []
cur = start
while len(ans) < N:
    ans.append(cur + 1)
    cur = order[cur]
print(*ans)
