D = int(input())
X = int(input())
S = [0, X]
for _ in range(D - 1):
    A = int(input())
    S.append(S[-1] + A)

Q = int(input())
for _ in range(Q):
    A, B = map(int, input().split())
    if S[A] == S[B]:
        print("Same")
    elif S[A] > S[B]:
        print(A)
    else:
        print(B)