N, M, K = map(int, input().split())
A = [input().split() for _ in range(M)]
for i in range(M):
    A[i] = [list(map(int, A[i][1:1+int(A[i][0])])), A[i][-1] == "o"]

ans = 0
for bit in range(2**N):
    is_real = [False] * N
    for i in range(N):
        if bit >> i & 1 == 1:
            is_real[i] = True

    ok = True
    for keys, result in A:
        cnt = 0

        for key in keys:
            key -= 1
            if is_real[key]:
                cnt += 1
        if (cnt >= K) != result:
            ok = False
            break

    if ok:
        ans += 1
print(ans)
