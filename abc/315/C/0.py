N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
A.sort(key=lambda x: -x[1])
first = 0
second = 1
for i in range(2, N):
    f, s = A[i]
    if f != A[first][0]:
        second = i
        break

ans = 0

for i in range(N):
    f, s = A[i]
    if i != first:
        if f == A[first][0]:
            ans = max(ans, s // 2 + A[first][1])
        else:
            ans = max(ans, s + A[first][1])

    if i != second:
        if f == A[second][0]:
            ans = max(ans, s // 2 + A[second][1])
        else:
            ans = max(ans, s + A[second][1])

print(ans)
