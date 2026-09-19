N, K = map(int, input().split())
A = list(map(int, input().split()))
A = list(set([x % K for x in A]))
A.sort()

ans = 10 ** 18

for i in range(len(A)):
    a = A[i]
    b = A[(i - 1) % len(A)]
    if a > b:
        b += K
    ans = min(ans, b - a)

print(ans)
