N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [0] # S[i] = [0, i)の合計
for x in A:
    S.append(S[-1] + x)

ans = []
head = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        head = (head + query[1]) % N
    else:
        L, R = query[1:]
        L -= 1
        R -= 1
        L += head
        R += head
        L %= N
        R %= N

        if head <= L <= R:
            ans.append(S[R + 1] - S[L])
        elif R < head <= L:
            ans.append(S[R + 1] + S[N] - S[L])
        else:
            ans.append(S[R + 1] - S[L])

for x in ans:
    print(x)