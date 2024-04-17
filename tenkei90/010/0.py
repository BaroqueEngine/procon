N = int(input())
c1 = []
c2 = []
for _ in range(N):
    C, P = map(int, input().split())
    if C == 1:
        c1.append(P)
        c2.append(0)
    else:
        c1.append(0)
        c2.append(P)

S1 = [0]
for x in c1:
    S1.append(S1[-1] + x)
S2 = [0]
for x in c2:
    S2.append(S2[-1] + x)

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    print(S1[R + 1] - S1[L], S2[R + 1] - S2[L])
