N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = 10**18
ans = 0
error = False

for x in range(10**6+1):
    y = INF
    ok = False
    for i in range(N):
        remain = Q[i] - A[i] * x
        if remain < 0:
            error = True
        if B[i] == 0:
            continue
        y = min(y, remain // B[i])
    if error:
        break
    ans = max(ans, x + y)

print(ans)
