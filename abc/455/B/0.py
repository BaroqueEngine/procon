H, W = map(int, input().split())
S = [input() for _ in range(H)]

def check(x, y, w, h):
    for ty in range(h):
        for tx in range(w):
            if S[y + ty][x + tx] != S[y + h - 1 - ty][x + w - 1 - tx]:
                return False

    return True

ans = 0
for y in range(H):
    for x in range(W):
        for h in range(1, H + 1 - y):
            for w in range(1, W + 1 - x):
                if check(x, y, w, h):
                    ans += 1

print(ans)
