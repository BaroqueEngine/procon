N, S, M, L = map(int, input().split())

ans = 10**18

for a in range(0, 20):
    for b in range(0, 20):
        for c in range(0, 20):
            if a * 6 + b * 8 + c * 12 >= N:
                ans = min(ans, a * S + b * M + c * L)
print(ans)
