N, M, K, Q = map(int, input().split())
C0 = []
C1 = []
for _ in range(N):
    P, T = map(int, input().split())
    if T == 0:
        C0.append(P)
    else:
        C1.append(P)
C0.sort()
C1.sort()

S0 = [0]
S1 = [0]
for x in C0:
    S0.append(S0[-1] + x)
for x in C1:
    S1.append(S1[-1] + x)

ans = 10**20
for i in range(min(M, len(C0)) + 1):
    buy0 = i
    buy1 = M - i
    if buy1 > len(C1):
        continue

    price = 0
    price += S0[buy0]
    price += S1[buy1]
    price += (buy1 + K - 1) // K * Q
    ans = min(ans, price)
print(ans)