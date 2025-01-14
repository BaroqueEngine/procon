A = list(map(int, input().split()))
H, W = A[:3], A[3:]

ans = 0
for a in range(1, 29):
    for b in range(1, 29):
        for e in range(1, 29):
            for i in range(1, 29):
                c = H[0] - (a + b)
                f = W[2] - (c + i)
                d = H[1] - (e + f)
                g = W[0] - (a + d)
                h = W[1] - (b + e)
                if c > 0 and f > 0 and d > 0 and g > 0 and h > 0 and (H[2] == g + h + i):
                    ans += 1

print(ans)
