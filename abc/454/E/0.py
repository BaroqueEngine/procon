T = int(input())
ans = []
for _ in range(T):
    N, ny, nx = map(int, input().split())
    ny -= 1
    nx -= 1
    if not(N % 2 == 0 and (nx + ny) % 2 == 1):
        ans.append("No")
        continue
    ans.append("Yes")
    route = []
    reversed = False
    for y in range(0, N, 2):
        if ny in [y, y + 1]:
            down = True
            for x in range(N):
                if x != nx:
                    if down:
                        route += ["D"]
                    else:
                        route += ["U"]
                    down = not down
                if x + 1 < N:
                    route += ["R"]
            reversed = True
        else:
            if reversed:
                route += ["L"] * (N - 1) + ["D"] + ["R"] * (N - 1)
            else:
                route += ["R"] * (N - 1) + ["D"] + ["L"] * (N - 1)
        if y + 2 < N:
            route += ["D"]
    ans.append("".join(route))

print("\n".join(ans))