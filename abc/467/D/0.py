ans = []

T = int(input())
for _ in range(T):
    px, py, qx, qy, rx, ry, sx, sy = map(int, input().split())

    ax, ay = px - qx, py - qy # 線分
    bx, by = -ay, ax # 垂直二等分線の向き
    cx, cy = px + qx, py + qy # 中点の2倍

    dx, dy = rx - sx, ry - sy # 線分
    ex, ey = -dy, dx  # 垂直二等分線の向き
    fx, fy = rx + sx, ry + sy # 中点の2倍

    # 外積による平行判定
    is_parallel = bx * ey - by * ex == 0
    if not is_parallel:
        ans.append("Yes")
    else:
        gx, gy = cx - fx, cy - fy # 通る点（中点）で出来るベクトル
        ans.append("Yes" if gx * by - bx * gy == 0 else "No") # 上記が、（どちらでもいいが）片方の垂直ベクトルと平行であるか？


for x in ans:
    print(x)