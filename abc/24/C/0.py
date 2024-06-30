N, D, K = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(D)]
T = [list(map(int, input().split())) for _ in range(K)]

ans = [10**18] * K

for i in range(D):
    L, R = S[i]
    for j in range(K):
        if T[j][0] == T[j][1]:
            continue
        # 移動可能なら
        if L <= T[j][0] <= R:
            # 右に移動する場合
            if T[j][0] < T[j][1]:
                T[j][0] = min(R, T[j][1])
            else:
                T[j][0] = max(L, T[j][1])
        if T[j][0] == T[j][1]:
            ans[j] = min(ans[j], i + 1)

for x in ans:
    print(x)
