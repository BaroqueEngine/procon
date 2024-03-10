H, W = map(int, input().split())
M = [list(input()) for _ in range(H)]
N = min(H, W)
cnt = [0] * N

for y in range(1, H - 1):
    for x in range(1, W - 1):
        if (
            M[y][x] == "#"
            and M[y][x]
            == M[y - 1][x - 1]
            == M[y - 1][x + 1]
            == M[y + 1][x - 1]
            == M[y + 1][x + 1]
        ):
            len = 0
            for i in range(1, 110):
                tx = x - i
                ty = y - i

                if tx < 0 or tx >= W or ty < 0 or ty >= H:
                    break
                if M[ty][tx] == ".":
                    break
                len += 1

            cnt[len - 1] += 1

print(*cnt)
