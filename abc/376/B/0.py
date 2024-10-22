N, Q = map(int, input().split())
pos = [1, 2]
ans = 0

for _ in range(Q):
    dir, num = input().split()
    target = int(num)

    # 左
    if dir == "L":
        move = 0
        fixed = 1
    else:
        move = 1
        fixed = 0

    i = pos[move]
    ok = True
    cnt = 0
    # 左に移動
    while True:
        if pos[fixed] == i:
            ok = False
            break
        if i == target:
            break
        cnt += 1
        i -= 1
        if i == 0:
            i = N

    if not ok:
        i = pos[move]
        cnt = 0
        # 右に移動
        while True:
            if i == target:
                break
            cnt += 1
            i += 1
            if i > N:
                i = 1

    ans += cnt
    pos[move] = target

print(ans)
