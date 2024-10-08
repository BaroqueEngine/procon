N = int(input())
K = list(map(int, input().split()))

ans = 10**18
for bit in range(2**N):
    A = 0
    B = 0
    for i in range(N):
        if (bit >> i) & 1 == 1:
            A += K[i]
        else:
            B += K[i]
    ans = min(ans, max(A, B))

print(ans)
