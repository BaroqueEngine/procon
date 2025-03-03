N = int(input())

arr = [["."] * N for _ in range(N)]

def fill(sx, sy, size):
    for y in range(sy, sy + size):
        arr[y][sx] = "#"
        arr[y][sx + size - 1] = "#"
    for x in range(sx, sx + size):
        arr[sy][x] = "#"
        arr[sy + size - 1][x] = "#"

pos = 0
while N > 0:
    fill(pos, pos, N)
    N -= 4
    pos += 2

for line in arr:
    print("".join(line))