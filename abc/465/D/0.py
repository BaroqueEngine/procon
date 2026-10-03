T = int(input())
ans = []
for _ in range(T):
    X, Y, K = map(int, input().split())
    route = [] # 根(0)までのルート
    while X > 0:
        route.append(X)
        X //= K
    route.append(0)
    route_set = set(route)

    y_down_cnt = 0
    while True:
        if Y in route_set:
            break
        Y //= K
        y_down_cnt += 1
    ans.append(route.index(Y) + y_down_cnt)

for x in ans:
    print(x) 