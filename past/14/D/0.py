H, A, B, C, D = map(int, input().split())

ans = 10**18
# アイテム2の使用回数
for i in range(31):
    hp = H
    for _ in range(i):
        hp = max(0, hp - C)
        if hp > 0:
            hp -= hp // 2
    # アイテム1の使用回数
    j = (hp + A - 1) // A
    cost = i * D + j * B
    ans = min(ans, cost)
print(ans)
