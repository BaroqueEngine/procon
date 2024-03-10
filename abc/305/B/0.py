A = [3, 1, 4, 1, 5, 9]
P, Q = input().split()
if P > Q:
    P, Q = Q, P


def to_number(c):
    return ord(c) - ord("A")


P = to_number(P)
Q = to_number(Q)

ans = 0
for i in range(P, Q):
    ans += A[i]
print(ans)
