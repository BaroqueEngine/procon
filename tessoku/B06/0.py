N = int(input())
A = list(map(int, input().split()))
S = [0]
for x in A:
    S.append(S[-1] + x)

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    num = R - L + 1
    atari = S[R + 1] - S[L]

    if atari > num // 2:
        print("win")
    elif num % 2 == 0 and num // 2 == atari:
        print("draw")
    else:
        print("lose")
