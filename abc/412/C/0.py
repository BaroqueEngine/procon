T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    if len(S) >= 3:
        T = [S[0]]
        for x in sorted(S[1:N-1]):
            if T[-1] * 2 >= S[-1]:
                break
            T.append(x)
        T += [S[-1]]
    else:
        T = S
    cnt = 2
    prev_i = 0
    i = 1
    while i < len(T):
        if T[prev_i] * 2 < T[i]:
            if prev_i + 1 == i:
                cnt = -1
                break
            cnt += 1
            prev_i = i - 1
            i -= 1
        i += 1
    ans.append(cnt)

for x in ans:
    print(x)