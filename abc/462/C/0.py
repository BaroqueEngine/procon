N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
G.sort()

ans = 1
min_y = G[0][1]

for x, y in G[1:]:
    if min_y > y:
        ans += 1
    min_y = min(min_y, y)

print(ans)