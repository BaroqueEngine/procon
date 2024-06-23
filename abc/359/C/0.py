sx, sy = map(int, input().split())
gx, gy = map(int, input().split())

# 右に移動することだけを考える
if sx > gx:
    sx, sy, gx, gy = gx, gy, sx, sy

# 最初に1マス無料で右に移動できるなら移動
if (sx < gx) and (sx % 2 == sy % 2):
    sx += 1

# 縦に1マス移動するたびに横にも1マス無料で移動することができる
sx = min(sx + abs(sy - gy), gx)

# 縦に移動
ans = abs(sy - gy)
sy = gy

# 一致済み（下の処理があるので、この処理多分いらない）
if sx == gx:
    print(ans)
    exit()

# 偶奇一致済み
if sx % 2 == gx % 2:
    ans += abs(sx - gx) // 2
    print(ans)
    exit()

# 横に1マス移動して偶奇を合わせる
# ブロックをまたぐか？
if sx % 2 != sy % 2:
    ans += 1
sx += 1

# 残りの横移動
ans += abs(sx - gx) // 2
print(ans)
