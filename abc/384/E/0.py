import heapq

H, W, X = map(int, input().split())
sy, sx = map(int, input().split())
sy -= 1
sx -= 1
S = [list(map(int, input().split())) for _ in range(H)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

seen = set([(sx, sy)])
q = []
for i in range(4):
    tx = sx + dx[i]
    ty = sy + dy[i]
    if tx < 0 or tx >= W or ty < 0 or ty >= H:
        continue
    heapq.heappush(q, (S[ty][tx], tx, ty))
    seen.add((tx, ty))
ans = S[sy][sx]

while len(q):
    power, x, y = heapq.heappop(q)
    # power < ans / X
    if power * X < ans:
        ans += power
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= W or ty < 0 or ty >= H:
                continue
            if (tx, ty) in seen:
                continue
            seen.add((tx, ty))
            heapq.heappush(q, (S[ty][tx], tx, ty))

print(ans)
