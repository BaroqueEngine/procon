N = int(input())
C = list(map(int, input().split()))

odd_min_i = 0
all_min_i = 0


def odd(index):
    return index % 2 == 0


for i in range(1, N):
    if C[i] < C[all_min_i]:
        all_min_i = i
    if odd(i) and C[i] < C[odd_min_i]:
        odd_min_i = i

set_cnt = 0
all_cnt = 0
ans = 0


def remain(index):
    return C[index] - all_cnt - set_cnt * odd(index)


Q = int(input())
for _ in range(Q):
    S = list(map(int, input().split()))
    if S[0] == 1:
        x, a = S[1:]
        x -= 1
        if remain(x) >= a:
            C[x] -= a
            ans += a
            if odd(x) and remain(x) < remain(odd_min_i):
                odd_min_i = x
            if remain(x) < remain(all_min_i):
                all_min_i = x
    elif S[0] == 2:
        a = S[1]
        if remain(odd_min_i) >= a:
            set_cnt += a
            ans += a * ((N + 1) // 2)
            if not odd(all_min_i) and remain(odd_min_i) < remain(all_min_i):
                all_min_i = odd_min_i
    else:
        a = S[1]
        if remain(all_min_i) >= a:
            all_cnt += a
            ans += a * N

print(ans)
