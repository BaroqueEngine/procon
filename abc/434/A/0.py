W, B = map(int, input().split())
W *= 1000

ans = (W + B - 1) // B
if ans * B == W:
    ans += 1

print(ans)